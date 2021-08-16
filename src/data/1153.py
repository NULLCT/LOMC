from sys import setrecursionlimit

setrecursionlimit(10**6)


def dfs(now, prev, d):
    depth[now] = d
    for nxt in edge[now]:
        if nxt != prev and depth[nxt] == -1:
            dfs(nxt, now, d + 1)


N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

depth = [-1] * N
dfs(0, -1, 0)

res = []
for _ in range(Q):
    c, d = map(int, input().split())
    if (depth[c - 1] + depth[d - 1]) % 2 == 0:
        res.append('Town')
    else:
        res.append('Road')

print(*res, sep='\n')
