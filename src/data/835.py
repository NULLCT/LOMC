from collections import defaultdict

adj = defaultdict(list)
N, Q = map(int, input().split())

for i in range(N - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

root = 0

stack = [root]
depth = [0 for _ in range(N)]
depth[0] = 0
visited = [0 for _ in range(N)]
visited[root] = 1

while (stack):
    v = stack.pop()

    for w in adj[v]:
        if visited[w] == 0:
            depth[w] = depth[v] + 1
            stack.append(w)
            visited[w] = 1

for i in range(Q):
    c, d = map(int, input().split())
    depth_c = depth[c - 1]
    depth_d = depth[d - 1]

    if (depth_c + depth_d) % 2 == 0:
        print("Town")
    else:
        print("Road")
