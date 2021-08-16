import collections

n, q = map(int, input().split())

g = []
for _ in range(n + 1):
    g.append([])

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n + 1)
visited[1] = True

queue = collections.deque([1])
dist = [0] * (n + 1)

while queue:
    flag = False
    que = queue.popleft()

    for k in g[que]:
        if visited[k]:
            continue
        else:
            visited[k] = True
            dist[k] += dist[que] + 1
            queue.append(k)

    if flag:
        break

for j in range(q):
    c, d = map(int, input().split())
    e = dist[c] - dist[d]
    if e % 2 == 0:
        print("Town")
    else:
        print("Road")
