n, q = map(int, input().split())
graph = [[] for _ in range(n)]
cnt = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    cnt.append(a)
    cnt.append(b)

from collections import Counter, deque

cnter = Counter(cnt)
for key, value in cnter.items():
    if value == 1:
        break

dist = [0 for _ in range(n)]
dist[key] = 1
que = deque([key])

while que:
    v1 = que.popleft()
    for v2 in graph[v1]:
        if dist[v2] == 0:
            dist[v2] = dist[v1] * (-1)
            que.append(v2)
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] == dist[d]:
        ans = 'Town'
    else:
        ans = 'Road'
    print(ans)
