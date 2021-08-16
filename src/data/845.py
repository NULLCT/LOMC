from collections import deque

n, q = map(int, input().split())
g = [[] for _ in range(n + 1)]
A = [0] * (n + 1)
for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)
    A[a] += 1
    A[b] += 1

x = A.index(1)
D = []


def bfs(u):
    queue = deque([u])
    d = [None] * (n + 1)  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


ans = bfs(x)
for i in range(q):
    c, d = map(int, input().split())
    val = ans[c] - ans[d]
    if val % 2 == 0:
        print("Town")
    else:
        print("Road")
