from queue import Queue
from collections import deque
import collections
import math
import sys

sys.setrecursionlimit(10000)


def comb(n, r):
    comb = 1
    r = min(r, n - r)
    for i in range(r):
        comb = comb * (n - i) // (i + 1)
    return comb


N, Q = map(int, input().split())
paths = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    paths[a].append(b)
    paths[b].append(a)

#bfs
q = collections.deque()
q.append(0)
visited = [False] * N
level = [0] * N
visited[0] = True
level[0] = 0
while len(q) != 0:
    node = q.popleft()
    for n in paths[node]:
        if not visited[n]:
            visited[n] = True
            q.append(n)
            level[n] = (level[node] + 1) % 2

for i in range(Q):
    c, d = map(int, input().split())
    if (level[c - 1] + level[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
