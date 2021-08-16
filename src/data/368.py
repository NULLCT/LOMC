from collections import deque

n, q = map(int, input().split())
graphs = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    graphs[a].append(b)
    graphs[b].append(a)
dist = [-1] * (n)
dist[0] = 0  #頂点0を親とする深さ優先探索

d = deque()
d.append(0)

while d:
    v = d.popleft()
    for i in graphs[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)
for j in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (abs((dist[c] - dist[d])) % 2 == 0):
        print("Town")
    else:
        print("Road")
