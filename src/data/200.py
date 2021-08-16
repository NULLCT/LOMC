from collections import deque

N, Q = map(int, input().split())
city = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    city[a - 1].append(b - 1)
    city[b - 1].append(a - 1)

# 道路は同じ長さ
# 街の数が奇数なら街で合い、偶数なら道路で会う


def bfs(s):
    seen = deque()
    seen.append(s)
    visited = [None] * N
    visited[s] = 1
    while seen:
        v = seen.popleft()
        for adj in city[v]:
            if visited[adj] is None:
                visited[adj] = visited[v] + 1
                seen.append(adj)
    return visited


dist = bfs(0)
for j in range(Q):
    c, d = map(int, input().split())
    diff = abs(dist[c - 1] - dist[d - 1]) + 1
    if diff % 2 == 0:
        print('Road')
    else:
        print('Town')
