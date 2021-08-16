import sys
import copy

sys.setrecursionlimit(10000000)
import math
import bisect
from collections import deque


def input():
    return sys.stdin.readline()[:-1]


N, Q = map(int, input().split())
g = [[] for i in range(N)]
C = []
D = []
tmp = [2 for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    g[a].append(b)
    g[b].append(a)

for i in range(Q):
    c, d = map(int, input().split())
    C.append(c - 1)
    D.append(d - 1)

que = deque([[0, 0]])
dist = [-1 for i in range(N)]
num = 0
dist[0] = 0
while que:
    tmp = que.popleft()
    jud = 0
    for i in g[tmp[0]]:
        if dist[i] == -1:
            dist[i] = tmp[1] + 1
            que.append([i, dist[i]])

#print(dist)

for i in range(Q):
    one = dist[C[i]]
    two = dist[D[i]]
    if abs(one - two) % 2 == 0:
        print("Town")
    else:
        print("Road")
