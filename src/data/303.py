import sys

sys.setrecursionlimit(500000)
n, q = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
c = [0] * q
d = [0] * q
for i in range(q):
    c[i], d[i] = map(int, input().split())
    c[i] -= 1
    d[i] -= 1
depth = [-1] * n


def dfs(v, e):
    depth[v] = e
    for w in adj[v]:
        if depth[w] == -1:
            dfs(w, e + 1)


dfs(0, 0)
for i in range(q):
    ans = depth[c[i]] - depth[d[i]]
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
