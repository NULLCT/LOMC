import sys

sys.setrecursionlimit(10**8)


def dfs(now, d):
    for i in g[now]:
        if i not in done:
            done.add(i)
            ds[i] = d + 1
            dfs(i, d + 1)


n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]

g = [[] for _ in range(n + 1)]
for a, b in ab:
    g[a].append(b)
    g[b].append(a)

ds = [None] * (n + 1)
ds[1] = 0
done = set([1])
dfs(1, 0)

for c, d in cd:
    if (ds[c] + ds[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
