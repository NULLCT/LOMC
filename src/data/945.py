#    ____                       _   _                _     _ _
#   / ___| __ _ _ __ __ _      | | | | __ _ _ __ ___| |__ (_) |_
#  | |  _ / _` | '__/ _` |_____| |_| |/ _` | '__/ __| '_ \| | __|
#  | |_| | (_| | | | (_| |_____|  _  | (_| | |  \__ \ | | | | |_
#   \____|\__,_|_|  \__, |     |_| |_|\__,_|_|  |___/_| |_|_|\__|
#                   |___/

from typing import Counter
import sys
from collections import defaultdict
from math import *
from collections import deque


def vinp():
    return map(int, input().split())


def linp():
    return list(map(int, input().split()))


def sinp():
    return input()


def inp():
    return int(input())


def mod(f):
    return f % 1000000007


def pr(*x):
    print(*x)


def finp():
    f = open("input.txt", "r")
    f = f.read().split("\n")
    return f


def finp():
    f = open("input.txt", "r")
    f = f.read().split("\n")
    return f


def fout():
    return open("output.txt", "w")


def fpr(f, x):
    f.write(x + "\n")


def csort(c):
    sorted(c.items(), key=lambda pair: pair[1], reverse=True)


def indc(l, n):
    c = {}
    for i in range(n):
        c[l[i]] = c.get(l[i], []) + [i + 1]
    return c


def LcA(a, b):
    for i in range(ma, -1, -1):
        if lc[a][i] != -1 and lc[a][i] != lc[b][i]:
            a = lc[a][i]
            b = lc[b][i]
    return lc[a][0]


def EQUAL(a, b):
    x, y = dis[a], dis[b]
    z = abs(x - y)
    if z == 0:
        return a, b
    if x > y:
        while z:
            p = int(log(z, 2))
            a = lc[a][p]
            z -= (1 << p)
    else:
        while z:
            p = int(log(z, 2))
            b = lc[b][p]
            z -= (1 << p)
    return a, b


n, qu = vinp()
d = defaultdict(list)
for i in range(n - 1):
    a, b = vinp()
    d[a].append(b)
    d[b].append(a)
dis = [0 for i in range(n + 1)]
q = deque()
q.append(1)
v = [0 for i in range(n + 1)]
ma = int(log(n, 2))
lc = [[-1 for i in range(ma + 1)] for j in range(n + 1)]
while q:
    a = q.popleft()
    v[a] = 1
    for i in d[a]:
        if not v[i]:
            v[i] = 1
            lc[i][0] = a
            q.append(i)
            dis[i] = dis[a] + 1
for j in range(1, ma + 1):
    for i in range(1, n + 1):
        if lc[i][j - 1] != -1:
            p = lc[i][j - 1]
            lc[i][j] = lc[p][j - 1]
ans = []
Q = [linp() for i in range(qu)]
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
