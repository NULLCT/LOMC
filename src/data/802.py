from collections import deque

n, q = map(int, input().split())

G = {i + 1: [] for i in range(n)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# Make node 1 the root
depth = {}
depth[1] = 0
to_visit = deque([1])
while to_visit:
    node = to_visit.popleft()
    for neighbour in G[node]:
        if neighbour not in depth:
            depth[neighbour] = depth[node] + 1
            to_visit.append(neighbour)

for _ in range(q):
    c, d = map(int, input().split())
    dist = abs(depth[c] - depth[d])
    if dist % 2 == 0:
        print("Town")
    else:
        print("Road")
