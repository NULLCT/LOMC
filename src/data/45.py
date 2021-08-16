from collections import deque

N, Q = map(int, input().split())
# 無向グラフの隣接リスト設定
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

dist = [-1] * (N + 1)
dist[1] = 0
q = deque([1])
while q:
    x = q.popleft()
    for y in graph[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)

for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c] - dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
