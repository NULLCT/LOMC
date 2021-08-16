from collections import deque

N, Q = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

# 深さを記録
depths = [-1] * N
queue = deque()
queue.append((0, 0))  # 頂点0を根とする
while len(queue) > 0:
    (node, depth) = queue.pop()
    depths[node] = depth
    for child in graph[node]:
        if depths[child] >= 0:
            continue
        queue.append((child, depth + 1))

for i in range(Q):
    c, d = map(int, input().split())
    if (depths[c - 1] + depths[d - 1]) % 2:
        print("Road")
    else:
        print("Town")