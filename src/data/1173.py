from collections import deque

N, Q = map(int, input().split())
E = [[] for n in range(N)]
for n in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)
Depth = [None for n in range(N)]
queue = deque([(0, 0)])
visited = [False for n in range(N)]
while queue:
    now, depth = queue.popleft()
    Depth[now] = depth
    visited[now] = True
    for e in E[now]:
        if not visited[e]:
            queue.append((e, depth + 1))
for q in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if Depth[c] % 2 == Depth[d] % 2:
        print("Town")
    else:
        print("Road")
