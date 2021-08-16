from collections import deque

N, Q = map(int, input().split())
E = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
CD = []

for i in range(Q):
    c, d = map(int, input().split())
    CD.append([c, d])

distance = [-1 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
q = deque()
q.append((1, 0))
visited[1] = True
while len(q) > 0:
    v, hop = q.pop()
    visited[v] = True
    distance[v] = hop
    for e in E[v]:
        if visited[e] == False:
            q.appendleft((e, hop + 1))

for i in range(Q):
    c, d = CD[i]
    temp = distance[c] + distance[d]
    if temp % 2 == 0:
        print("Town")
    else:
        print("Road")
