from collections import deque

n, q = map(int, input().split())
cl, dl = [], []

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for _ in range(q):
    tc, td = map(int, input().split())
    cl.append(tc)
    dl.append(td)

dist = [-1] * (n + 1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

ans = dist[1:]

for i, j in zip(cl, dl):
    if abs(ans[i - 1] - ans[j - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
