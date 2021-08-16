import sys

sys.setrecursionlimit(10**7)

n, q = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1] += [b - 1]
    g[b - 1] += [a - 1]

visited = [-1] * n
visited[0] = 0


def dfs(v, p, res):
    if p != -1:
        visited[v] = visited[p] ^ 1
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v, visited)
    return


dfs(0, -1, visited)

for _ in range(q):
    c, d = map(int, input().split())
    if visited[c - 1] == visited[d - 1]:
        print('Town')
    else:
        print('Road')
