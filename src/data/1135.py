from sys import setrecursionlimit

setrecursionlimit(10**7)

N, Q = [int(x) for x in input().split()]
to = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = [int(x) - 1 for x in input().split()]
    to[a].append(b)
    to[b].append(a)

depth = [-1] * N


def dfs(v, p, d):
    depth[v] = d
    for u in to[v]:
        if u == p: continue
        dfs(u, v, d + 1)


dfs(0, -1, 0)

for _ in range(Q):
    c, d = [int(x) - 1 for x in input().split()]
    ans = (depth[c] - depth[d]) % 2
    print('Road' if ans else 'Town')
