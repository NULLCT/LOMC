from collections import deque

n, q = map(int, input().split())

g = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(u):
    queue = deque([u])
    d = [None] * (n + 2)
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


x = bfs(1)
for i in range(q):
    c, d = map(int, input().split())

    if (x[c] + x[d]) % 2 == 1:

        print("Road")
    else:
        print("Town")
