from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * N
# pre=[-1]*N
dist[0] = 0

q = deque()
q.append(0)

while q:
    v = q.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        else:
            dist[i] = dist[v] + 1
            # pre[i]=v
            q.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    if abs(dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
