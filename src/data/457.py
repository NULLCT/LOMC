from collections import deque

N, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# ab=[]
cd = []

# for i in range(N-1):
#     ab.append(list(map(int,input().split())))

for i in range(Q):
    cd.append(list(map(int, input().split())))

dist = [-1] * (N + 1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    # print("v",v)
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

for i in range(Q):
    if abs(dist[cd[i][0]] - dist[cd[i][1]]) % 2 == 0:
        print("Town")
    else:
        print("Road")
