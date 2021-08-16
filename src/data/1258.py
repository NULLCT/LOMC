from heapq import heappop, heappush

N, Q = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
color = [-1] * N
color[0] = 0
q = [0]
while q:
    now = heappop(q)
    for to in graph[now]:
        if color[to] == -1:
            color[to] = 1 - color[now]
            heappush(q, to)
#print(color)
for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
