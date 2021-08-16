from collections import deque

n, q = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def bfs(u):
    queue = deque([u])
    d = [None] * n
    d[u] = 0

    while queue:
        v = queue.popleft()
        for j in G[v]:
            if d[j] == None:
                d[j] = (d[v] + 1) % 2
                queue.append(j)
    return d


dis = bfs(0)

for j in range(q):
    q1, q2 = map(int, input().split())
    if dis[q1 - 1] != dis[q2 - 1]:
        print("Road")
    else:
        print("Town")
