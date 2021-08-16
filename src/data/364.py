n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dep = [-1 for _ in range(n + 1)]
from collections import deque

que = deque()
que.append((1, 0))
while len(que) > 0:
    (node, depth) = que.pop()
    dep[node] = depth
    for g in graph[node]:
        if dep[g] >= 0:
            continue
        que.append((g, depth + 1))

for i in range(q):
    c, d = map(int, input().split())
    if (dep[c] + dep[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
