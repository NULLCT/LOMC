import sys

sys.setrecursionlimit(100000)

n, q = map(int, input().split())

con = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    con[a - 1].append(b - 1)
    con[b - 1].append(a - 1)

dep = [-1 for i in range(n)]


def dfs(v, p=-1, depth=0):
    dep[v] = depth
    for i in con[v]:
        if i == p:
            continue
        else:
            dfs(i, v, depth + 1)


dfs(0)

for i in range(q):
    c, d = map(int, input().split())
    sub = dep[c - 1] - dep[d - 1]
    print("Town" if sub % 2 == 0 else "Road")
