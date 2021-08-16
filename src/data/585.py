import sys

sys.setrecursionlimit(10**6)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

cd = [list(map(int, input().split())) for i in range(q)]
cd = [[x - 1, y - 1] for x, y in cd]
ds = [0] * n


def f(s, p):
    if p == -1: ds[s] = 0
    else: ds[s] = ds[p] + 1
    for u in g[s]:
        if u != p: f(u, s)


f(0, -1)

for c, d in cd:
    if abs(ds[c] - ds[d]) % 2: print("Road")
    else: print("Town")
