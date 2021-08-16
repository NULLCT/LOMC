from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
dist = [10**18] * n
dist[0] = 0
p = deque()
p.append(0)
while len(p) > 0:
    x = p.popleft()
    for y in graph[x]:
        if dist[y] > dist[x] + 1:
            dist[y] = dist[x] + 1
            p.append(y)
ans = []
for _ in range(q):
    c, d = map(int, input().split())
    if (dist[c - 1] + dist[d - 1]) % 2 == 0:
        ans.append("Town")
    else:
        ans.append("Road")
print(*ans, sep="\n")
