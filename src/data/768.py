from collections import deque

n, q = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
l = [0] * n


def bfs(u):
    queue = deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


l = bfs(0)
for i in range(q):
    c, d = list(map(int, input().split()))
    c -= 1
    d -= 1
    k = l[c] - l[d]
    if k % 2 == 1:
        print("Road")
    else:
        print("Town")
