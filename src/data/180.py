import sys

sys.setrecursionlimit(1000000000)

n, nq = map(int, input().split())
g = [[] for _ in range(n)]
q = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

for _ in range(nq):
    q.append(list(map(int, input().split())))

color = [0 for _ in range(n)]


def dfs(x, cnt):
    if cnt % 2 == 1: color[x] = 1
    else: color[x] = -1
    for next in g[x]:
        if color[next] != 0: continue
        dfs(next, cnt + 1)


dfs(0, 1)

for x, y in q:
    if color[x - 1] == color[y - 1]: print('Town')
    else: print('Road')
