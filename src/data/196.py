import sys

N, Q = map(int, input().split())
sys.setrecursionlimit(N + 2)
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
d = [None] * N


def dfs(u, p, depth):
    d[u] = depth % 2
    for v in G[u]:
        if p != v:
            dfs(v, u, depth + 1)


dfs(0, -1, 0)
for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    print('Town' if (d[u] + d[v]) % 2 == 0 else 'Road')
