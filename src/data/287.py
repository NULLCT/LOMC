# -*- coding: UTF-8 -*-

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
adj = [[] for n in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def BFS(vnum, sv, adj):
    from collections import deque
    dist = [-1] * (vnum + 1)
    dist[sv] = 0
    que = deque([sv])
    while que:
        v = que.popleft()
        for x in adj[v]:
            if not dist[x] == -1:
                continue
            dist[x] = dist[v] + 1
            que.append(x)
    return dist[1:]


first_bfs = BFS(N, 1, adj)
for q in range(Q):
    c, d = map(int, input().split())
    if abs(first_bfs[c - 1] - first_bfs[d - 1]) % 2:
        print('Road')
    else:
        print('Town')
