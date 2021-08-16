from collections import deque

N, Q = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

depths = [-1 for _ in range(N + 1)]

queue = deque()
queue.append((1, 0))
while len(queue) > 0:
    (node, depth) = queue.pop()
    depths[node] = depth
    for child in graph[node]:
        if depths[child] >= 0:
            continue
        queue.append((child, depth + 1))

for query in range(Q):
    c, d = list(map(int, input().split()))
    if (depths[c] + depths[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
