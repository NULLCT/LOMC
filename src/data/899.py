import sys
from collections import defaultdict
from math import inf

n, q = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
dist = [inf] * (n + 2)
dist[1] = 0

# iterative dfs
to_visit = [[1, -1]]
while to_visit:
    c, v = to_visit.pop()
    if v != -1:
        dist[c] = dist[v] + 1
    for u in g[c]:
        if u == v: continue
        to_visit.append([u, c])

for i in range(q):
    c, d = list(map(int, input().split()))
    distance = dist[c] + dist[d]
    if distance % 2 == 1:
        print("Road")
    else:
        print("Town")
