import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

depth = [0] * (n + 1)


def dfs(cur, last=-1):
    for next in g[cur]:
        if next == last:
            continue
        depth[next] = depth[cur] + 1
        dfs(next, cur)


dfs(1)

for i in range(m):
    c, d = map(int, input().split())
    if (depth[c] - depth[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
