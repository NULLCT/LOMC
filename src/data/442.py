N, Q = map(int, input().split())
L = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    L[a].append(b)
    L[b].append(a)
#print(L)
from collections import deque

q = deque([0])
visited = [False] * N
visited[0] = True
dist = [0] * N
while q:
    r = q.popleft()
    #print(r,q)
    for to in L[r]:
        if visited[to]:
            continue
        visited[to] = True
        dist[to] = dist[r] + 1
        q.append(to)
#print(dist)
for i in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    w1 = dist[c]
    w2 = dist[d]
    #print(w,c,d)
    if (w1 + w2) % 2 == 0:
        print("Town")
    else:
        print("Road")
