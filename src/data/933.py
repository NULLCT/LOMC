from collections import deque

n, q = map(int, input().split())

edges = [list() for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
# print(edges)

depth = 0
queue = deque([[0, -1, 0]])
dist = [0] * n

while queue:
    node, parent, depth = queue.popleft()
    dist[node] = depth

    for child in edges[node]:
        if child != parent:
            queue.append([child, node, depth + 1])
# print(dist)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
