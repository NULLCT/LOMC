import sys

sys.setrecursionlimit(10**7)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

used = [0] * N
dist = [-1] * N


def dfs(v, p):
    used[v] = 1
    dist[v] = dist[p] + 1
    for w in G[v]:
        if used[w]:
            continue

        dfs(w, v)


dfs(0, 0)  # 最初だけ注意
for i in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2:
        print('Road')
    else:
        print('Town')
