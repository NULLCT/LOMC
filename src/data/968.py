import sys

input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)


def bfs():
    q = deque([0])
    seen = [-1] * N
    seen[0] = 0
    while q:
        i = q.popleft()
        for j in G[i]:
            if seen[j] != -1:
                continue
            seen[j] = seen[i] + 1
            q.append(j)
    return seen


dist = bfs()
for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if abs(dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
