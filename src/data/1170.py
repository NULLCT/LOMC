from collections import deque

N, Q = map(int, input().split())
ways = [[] for _ in range(N + 1)]
dist = [-1 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    ways[a].append(b)
    ways[b].append(a)

stack = deque([1])
dist[1] = 0
while stack:
    t = stack.pop()
    for j in ways[t]:
        if dist[j] == -1:
            dist[j] = (dist[t] + 1) % 2
            stack.append(j)
for _ in range(Q):
    c, d = map(int, input().split())
    if dist[c] == dist[d]:
        print("Town")
    else:
        print("Road")
