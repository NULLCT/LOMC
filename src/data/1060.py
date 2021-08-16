from collections import deque

n, q = map(int, input().split())
P = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    P[a - 1].append(b - 1)
    P[b - 1].append(a - 1)


def bfs(u):
    queue = deque([u])
    d = [None] * n
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in P[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


L = bfs(0)

for i in range(q):
    c, d = map(int, input().split())
    print("Town" if (L[c - 1] - L[d - 1]) % 2 == 0 else "Road")
