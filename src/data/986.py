'''                      __      __        __                  __    __        __  __       
                      /  |    /  |      /  |                /  |  /  |     /   |/| |      
  _______   ______   _$$ |_   $$ |____  $$ |____    ______  $$/   _$$ |_    $$/ |$$ |   __ 
 /       | /       / $$   |  $$         $$        /         /  | / $$   |   /  |$$ |  /  |
/$$$$$$$/ /$$$$$$  |$$$$$$/   $$$$$$$  |$$$$$$$  |/$$$$$$  |$$ | $$$$$$/   $$  |$$ |_/$$/ 
$$        $$    $$ |  $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ | __  $$  |$$   $$<  
 $$$$$$  |$$$$$$$$/   $$ |/  |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |/  | $$  |$$$$$$  \
/     $$/ $$       |  $$  $$/ $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$  $$/  $$  |$$ | $$  |
$$$$$$$/   $$$$$$$/    $$$$/  $$/   $$/ $$/   $$/ $$/       $$/    $$$$/   $$/ |$$/   $$/ 
                                                                                        
'''

import sys
from os import path
import bisect
if (path.exists('input.txt')):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output1.txt', 'w')
from heapq import heappop, heappush, heapify
from math import ceil, log
from collections import defaultdict, deque

maxi = sys.maxsize
mini = -maxi
from math import gcd

n, qu = map(int, input().split())
d = defaultdict(list)
for i in range(n - 1):
    x, y = map(int, input().split())
    d[x].append(y)
    d[y].append(x)
v = [0 for i in range(n + 1)]
maxi = int(log(n, 2))
dis = [0 for i in range(n + 1)]
q = deque()
q.append(1)
LCA = [[-1 for i in range(maxi + 1)] for j in range(n + 1)]
while q:
    a = q.popleft()
    v[a] = 1
    for i in d[a]:
        if not v[i]:
            v[i] = 1
            LCA[i][0] = a
            q.append(i)
            dis[i] = dis[a] + 1
for j in range(1, maxi + 1):
    for i in range(1, n + 1):
        if LCA[i][j - 1] != -1:
            p = LCA[i][j - 1]
            LCA[i][j] = LCA[p][j - 1]


def solve(a, b):
    for i in range(maxi, -1, -1):
        if LCA[a][i] != -1 and LCA[a][i] != LCA[b][i]:
            a = LCA[a][i]
            b = LCA[b][i]
    return LCA[a][0]


ans = []
Q = [list(map(int, input().split())) for i in range(qu)]


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
    z = solve(x, y)
    vp = dis[a] + dis[b] - (2 * dis[z])
    if vp % 2:
        ans.append('Road')
    else:
        ans.append('Town')
for i in ans:
    print(i)
