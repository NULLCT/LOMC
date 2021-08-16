N, X = map(int, input().split())

import sys

sys.setrecursionlimit(1000000)
G = []
for i in range(N):
    G.append([])

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

from collections import deque

visited = [False] * N

Q = deque()
Q.append(0)
visited[0] = True
dis = [0] * N

while len(Q) > 0:
    i = Q.popleft()
    for j in G[i]:
        if not visited[j]:
            visited[j] = True
            dis[j] = dis[i] + 1
            Q.append(j)

for i in range(X):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    tmp = dis[c] + dis[d]
    if tmp % 2 == 1:
        print('Road')
    else:
        print('Town')
