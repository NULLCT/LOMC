n, q = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]
import sys

sys.setrecursionlimit(10**9)

from collections import defaultdict

g = defaultdict(list)
for a, b in ab:
    g[a] += [b]
    g[b] += [a]

cs = [-1] * (n + 1)


def dfs(u, c):
    que = [(u, c)]

    while len(que) > 0:
        u, c = que.pop()
        if cs[u] == -1:
            cs[u] = c
            for v in g[u]:
                que += [(v, 1 - c)]


dfs(1, 0)

for c, d in cd:
    if cs[c] == cs[d]:
        print("Town")
    else:
        print("Road")
