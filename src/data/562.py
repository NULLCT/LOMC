from sys import setrecursionlimit

setrecursionlimit(10**6)

N, Q, *I = map(int, open(0).read().split())
AB, CD = I[:2 * (N - 1)], I[2 * (N - 1):]

E = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(AB)] * 2):
    E[a].append(b)
    E[b].append(a)

dist = [0] * (N + 1)


def dfs(cur, par):
    d = dist[cur]
    for nxt in E[cur]:
        if nxt != par:
            dist[nxt] = 1 + d
            dfs(nxt, cur)


dfs(1, 0)

for c, d in zip(*[iter(CD)] * 2):
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
