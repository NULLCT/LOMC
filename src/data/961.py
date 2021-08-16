from collections import deque

n, Q = map(int, input().split())
data = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
dist = [-1] * (n + 1)
dist[1] = 0
q = deque()
q.append(1)
while q:
    now = q.pop()
    for to in data[now]:
        if dist[to] != -1:
            continue
        dist[to] = dist[now] + 1
        q.append(to)
for i in range(Q):
    c, d = map(int, input().split())
    if dist[c] % 2 == 0 and dist[d] % 2 == 0:
        print("Town")
    elif dist[c] % 2 == 1 and dist[d] % 2 == 1:
        print("Town")
    else:
        print("Road")
