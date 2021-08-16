from collections import deque

N, Q = map(int, input().split())

tree = [[] for _ in range(N)]
ans = []

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)


def bfs(u):
    queue = deque([u])
    d = [None] * (N)
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if d[i] is not None:
                continue
            d[i] = d[v] + 1
            queue.append(i)
    return d


dis = bfs(0)

for _ in range(Q):
    c, d = map(int, input().split())
    if (dis[c - 1] + dis[d - 1]) % 2 == 0:
        ans.append("Town")
    else:
        ans.append("Road")

print(*ans, sep="\n")
