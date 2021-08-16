from collections import deque
from sys import stderr

INF = 1 << 60

N, Q = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

depth = [INF] * (N + 1)
depth[1] = 0

s = deque([1])
while s:
    p = s.pop()
    for n in edges[p]:
        if depth[n] > depth[p] + 1:
            depth[n] = depth[p] + 1
            s.append(n)

for _ in range(Q):
    c, d = map(int, input().split())
    print("Road" if (depth[c] + depth[d]) % 2 else "Town", flush=False)
