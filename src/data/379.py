n, q = map(int, input().split())
G = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

query = []
for i in range(q):
    query.append(list(map(int, input().split())))

from collections import deque


#引数はリストと開始点
def bfs(graph, first):
    que = deque()
    dist[first] = 0
    que.append(first)

    while que:
        v = que[0]
        que.popleft()

        for i in graph[v]:
            if (dist[i] != -1):
                continue

            dist[i] = dist[v] + 1
            que.append(i)
    return dist


dist = [-1] * n
bfs(G, 0)
for i in query:
    if (dist[i[0] - 1] + dist[i[1] - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
