import collections

N, Q = map(int, input().split())
# ab=[list(map(int,input().split())) for _ in range(N-1)]

graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (N + 1)
dist[0] = 0
dist[1] = 0

d = collections.deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

dist = dist[1:]

for i in range(Q):
    c, d = map(int, input().split())
    num = dist[d - 1] - dist[c - 1]
    print('Town' if num % 2 == 0 else 'Road')
