from collections import deque

d = deque()

N, Q = map(int, input().split())
route = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    route[a - 1].append(b - 1)
    route[b - 1].append(a - 1)

# BFS
cost_from_start = [-1] * N
cost_from_start[0] = 0
d.append((0, 0))

while len(d) > 0:
    current_node, cost = d.popleft()
    cost_from_start[current_node] = cost

    for next_node in route[current_node]:
        if cost_from_start[
                next_node] == -1 or cost_from_start[next_node] > cost + 1:
            d.append((next_node, cost + 1))

for i in range(Q):
    c, d = map(int, input().split())
    if abs(cost_from_start[c - 1] - cost_from_start[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
