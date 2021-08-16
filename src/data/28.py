from sys import setrecursionlimit

setrecursionlimit(10**6)


def dfs(pos, pre):
    for i in G[pos]:
        if i == pre:
            continue
        dist[i] = dist[pos] ^ 1
        dfs(i, pos)


N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dist = [0] * N
dfs(0, 0)
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
