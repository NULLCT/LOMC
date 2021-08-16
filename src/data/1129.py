import collections, sys

sys.setrecursionlimit(10**8)

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dist = [-1] * N

q = collections.deque([0])

while q:
    v = q.popleft()
    for n_v in graph[v]:
        if dist[n_v] != -1: continue
        dist[n_v] = dist[v] + 1
        q.append(n_v)

# dist[0] = 0

# def DFS(v):
# 	for n_v in graph[v]:
# 		if dist[n_v] != -1: continue
# 		dist[n_v] = dist[v] + 1
# 		DFS(n_v)

# DFS(0)

for _ in range(Q):
    c, d = map(int, input().split())
    if dist[c - 1] + dist[d - 1] & 1:
        print('Road')
    else:
        print('Town')
