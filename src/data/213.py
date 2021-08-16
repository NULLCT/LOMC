from collections import deque

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]

graph = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

colors = [0 for _ in range(N)]
colors[0] = 1
Q = deque()
Q.append(0)
while len(Q) > 0:
    i = Q.popleft()
    for j in graph[i]:
        if colors[j] == 0:
            colors[j] = (-1) * colors[i]
            Q.append(j)
for c, d in CD:
    c -= 1
    d -= 1
    if colors[c] == colors[d]:
        print("Town")
    else:
        print("Road")
