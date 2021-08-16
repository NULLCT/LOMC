import collections

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0] * (n + 1)
visited[1] = 1
dist = [0] * (n + 1)
que = collections.deque([1])

while que:
    q = que.popleft()
    for i in g[q]:
        if visited[i] == 0:
            visited[i] = 1
            que.append(i)
            dist[i] = dist[q] + 1

for i in range(m):
    c, d = map(int, input().split())
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
