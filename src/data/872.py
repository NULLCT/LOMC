#!/usr/bin/env python3
N, Q = map(int, input().split())
AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N - 1)]
CD = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

from collections import deque

G = [[] for _ in range(N)]
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

start = 0
dist = [-1] * N
Q = deque()
Q.append(start)
dist[start] = 0
while Q:
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)

for c, d in CD:
    if abs(dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")

# D = [[-1]*N for _ in range(N)]

# for start in range(N):
#     dist = [-1]*N
#     Q = deque()
#     Q.append(start)
#     dist[start] = 0
#     while Q:
#         i = Q.popleft()
#         for j in G[i]:
#             if dist[j] == -1:
#                 dist[j] = dist[i] + 1
#                 Q.append(j)
#     for j in range(N):
#         D[start][j] = dist[j]

# for c, d in CD:
#     if D[c][d] % 2 == 0:
#         print("Town")
#     else:
#         print("Road")
