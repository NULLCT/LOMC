import sys
from collections import deque

sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
d = deque()
d.append((0, 0))
depth = [-1] * N
while d:
    i, dep = d.popleft()
    if depth[i] > -1:
        pass
    else:
        depth[i] = dep
        for node in graph[i]:
            d.append((node, dep + 1))
for _ in range(M):
    c, d = map(int, input().split())
    if (depth[c - 1] + depth[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
