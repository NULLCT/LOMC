from collections import deque

N, Q = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

dq = deque([])
node = 0
depth = 1
dq.append((node, depth))

dps_list = [-1 for _ in range(N)]
dps_list[node] = 0

while len(dq) != 0:
    node, depth = dq.popleft()
    for child in graph[node]:
        if dps_list[child] == -1:
            dps_list[child] = depth
            dq.append((child, depth + 1))

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    depth_sa = abs(dps_list[c] - dps_list[d])
    if depth_sa % 2 == 0:
        print("Town")
    else:
        print("Road")
