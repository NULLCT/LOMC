import sys

sys.setrecursionlimit(10**6)

n, q = map(int, input().split())

edge = [[] for _ in range(n)]
dep = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


def dfs(x, last=-1):
    for to in edge[x]:
        if to == last:
            continue
        dep[to] = dep[x] + 1
        dfs(to, x)


dfs(0)

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dep[c] % 2 == dep[d] % 2:
        print('Town')
    else:
        print('Road')
