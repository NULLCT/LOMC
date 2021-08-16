import sys


def dfs(prev, now, visited, flag):
    visited[now] = True
    for nxt in G[now]:
        if nxt == prev or visited[nxt]:
            continue
        res[nxt] = not flag
        dfs(now, nxt, visited, not flag)


sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
a, b = zip(*[tuple(map(int, input().split())) for _ in range(n - 1)])
c, d = zip(*[tuple(map(int, input().split())) for _ in range(q)])

# 距離の偶奇が重要？
# 2色？に分ける

G = [[] for _ in range(n)]
for i in range(n - 1):
    G[a[i] - 1].append(b[i] - 1)
    G[b[i] - 1].append(a[i] - 1)

visited = [False] * n
res = [False] * n
dfs(0, 0, visited, False)
for i in range(q):
    if res[c[i] - 1] ^ res[d[i] - 1]:
        print("Road")
    else:
        print("Town")
