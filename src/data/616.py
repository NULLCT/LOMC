from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())

G = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

depth = [-1] * N
depth[0] = 0

q = [0]
while q:
    at = q.pop()
    for to in G[at]:
        if depth[to] != -1:
            continue
        depth[to] = depth[at] + 1
        q.append(to)

for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if depth[c] % 2 == depth[d] % 2:
        print("Town")
    else:
        print("Road")
