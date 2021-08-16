n, q = map(int, input().split())

e = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

import sys

sys.setrecursionlimit(100000000)
d = [-1] * n
d[0] = 0


def dfs(v):
    for u in e[v]:
        if d[u] >= 0:
            continue
        d[u] = d[v] + 1
        dfs(u)


dfs(0)

for _ in range(q):
    c, dd = map(int, input().split())
    c -= 1
    dd -= 1
    if (d[c] - d[dd]) % 2:
        print("Road")
    else:
        print("Town")
