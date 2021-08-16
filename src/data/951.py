import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

N, Q, *X = list(map(int, open(0).read().split()))
a, b = X[0::2][:N - 1], X[1::2][:N - 1]
c, d = X[0::2][N - 1:], X[1::2][N - 1:]

g = defaultdict(list)

for aa, bb in zip(a, b):
    g[aa].append(bb)
    g[bb].append(aa)

result = [-1] * (N + 1)


def dfs(curr):
    v = g[curr]
    for vv in v:
        if result[vv] < 0:
            result[vv] = result[curr] + 1
            dfs(vv)


dfs(1)

for cc, dd in zip(c, d):
    print("Town" if (result[cc] - result[dd]) % 2 == 0 else "Road")
