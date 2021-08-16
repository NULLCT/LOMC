n, q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n - 1)]
cd = [list(map(int, input().split())) for i in range(q)]
import sys

sys.setrecursionlimit(10**7)
from collections import defaultdict

roads = defaultdict(list)
for a, b in ab:
    roads[a - 1].append(b - 1)
    roads[b - 1].append(a - 1)

color = [-10**10] * n


def dfs(maenoiro, gen):
    color[gen] = not maenoiro
    for i in roads[gen]:
        if color[i] < 0:
            dfs(color[gen], i)


dfs(1, 0)

for c, d in cd:
    c, d = c - 1, d - 1
    print("Road" if color[c] != color[d] else "Town")
