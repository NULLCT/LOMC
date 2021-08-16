from collections import deque

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda n: int(n) - 1, input().split())
    edge[x].append(y)
    edge[y].append(x)

# seen = [0] * N
# depth_from_root = {}
depth_from_root = [-1] * N
queue = deque([(0, 0)])
while queue:
    now, depth = queue.popleft()
    # if seen[now]:
    #     continue
    if depth_from_root[now] != -1:
        continue
    # seen[now] = 1
    depth_from_root[now] = depth
    for n_node in edge[now]:
        # if seen[n_node]:
        #     continue
        if depth_from_root[n_node] != -1:
            continue
        queue.append((n_node, depth + 1))

for _ in range(Q):
    c, d = map(lambda n: int(n) - 1, input().split())

    if abs(depth_from_root[c] - depth_from_root[d]) % 2:
        print("Road")
    else:
        print("Town")
