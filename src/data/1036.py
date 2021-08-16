#                _          _                                        _
#   ___ ___   __| | ___  __| |_ __ ___  __ _ _ __ ___   ___ _ __  __| | __ _
#  / __/ _ \ / _` |/ _ \/ _` | '__/ _ \/ _` | '_ ` _ \ / _ \ '__|/ _` |/ _` |
# | (_| (_) | (_| |  __/ (_| | | |  __/ (_| | | | | | |  __/ |  | (_| | (_| |
#  \___\___/ \__,_|\___|\__,_|_|  \___|\__,_|_| |_| |_|\___|_|___\__,_|\__, |
#                                                           |_____|    |___/
from sys import *
'''sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w') '''
from collections import defaultdict as dd
from collections import deque
from math import *
from bisect import *


#sys.setrecursionlimit(10 ** 8)
def sinp():
    return input()


def inp():
    return int(sinp())


def minp():
    return map(int, sinp().split())


def linp():
    return list(minp())


def strl():
    return list(sinp())


def pr(x):
    print(x)


def EQUAL(a, b):
    x, y = dis[a], dis[b]
    z = abs(x - y)
    if z == 0:
        return a, b
    if x > y:
        while z:
            p = int(log(z, 2))
            a = LCA[a][p]
            z -= (1 << p)
    else:
        while z:
            p = int(log(z, 2))
            b = LCA[b][p]
            z -= (1 << p)
    return a, b


def LcA(a, b):
    for i in range(maxN, -1, -1):
        if LCA[a][i] != -1 and LCA[a][i] != LCA[b][i]:
            a = LCA[a][i]
            b = LCA[b][i]
    return LCA[a][0]


mod = int(1e9 + 7)
n, Q = minp()
d = dd(list)
for i in range(n - 1):
    a, b = minp()
    d[a].append(b)
    d[b].append(a)
dis = [0 for i in range(n + 1)]
q = deque()
q.append(1)
v = [0 for i in range(n + 1)]
maxN = int(log(n, 2))
LCA = [[-1 for i in range(maxN + 1)] for j in range(n + 1)]
while q:
    a = q.popleft()
    v[a] = 1
    for i in d[a]:
        if not v[i]:
            v[i] = 1
            LCA[i][0] = a
            q.append(i)
            dis[i] = dis[a] + 1
for j in range(1, maxN + 1):
    for i in range(1, n + 1):
        if LCA[i][j - 1] != -1:
            p = LCA[i][j - 1]
            LCA[i][j] = LCA[p][j - 1]
ans = []
Q = [linp() for i in range(Q)]
for i in Q:
    a, b = i
    x, y = EQUAL(a, b)
    if x == y:
        vp = dis[a] + dis[b] - (2 * dis[y])
        if vp % 2:
            ans.append('Road')
        else:
            ans.append('Town')
        continue
    z = LcA(x, y)
    vp = dis[a] + dis[b] - (2 * dis[z])
    if vp % 2:
        ans.append('Road')
    else:
        ans.append('Town')
pr('\n'.join(ans))
