from collections import deque

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda n: int(n) - 1, input().split())
    edge[x].append(y)
    edge[y].append(x)  # 有向グラフならこの行は消す!!

seen = [0] * N
node_to_depth = {}
queue = deque([(0, 0)])
while queue:
    now, depth = queue.popleft()
    if seen[now]:
        continue
    seen[now] = 1
    node_to_depth[now] = depth
    for n_node in edge[now]:
        if seen[n_node]:
            continue
        queue.append((n_node, depth + 1))

for _ in range(Q):
    c, d = map(lambda n: int(n) - 1, input().split())

    if abs(node_to_depth[c] - node_to_depth[d]) % 2:
        print("Road")
    else:
        print("Town")
