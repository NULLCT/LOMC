import sys

sys.setrecursionlimit(10**7)


def dfs(depth, depths, node, parent, g):
    depths[node] = depth
    depth += 1
    for nex in g[node]:
        if nex == parent:
            continue
        dfs(depth, depths, nex, node, g)


n, q = map(int, input().split())
g = [[] for _ in range(n)]
depths = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

dfs(0, depths, 0, 0, g)
for _ in range(q):
    c, d = map(int, input().split())
    if abs(depths[c - 1] - depths[d - 1]) & 1:
        print('Road')
    else:
        print('Town')
