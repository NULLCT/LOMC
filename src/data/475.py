n, q = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
c = [0] * q
d = [0] * q
for i in range(q):
    c[i], d[i] = map(int, input().split())
    c[i] -= 1
    d[i] -= 1

from collections import deque

dist = [-1] * n
que = deque([0])
dist[0] = 0
while que:
    v = que.popleft()
    e = dist[v]
    for w in adj[v]:
        if dist[w] > -1:
            continue
        dist[w] = e + 1
        que.append(w)

for i in range(q):
    ans = dist[c[i]] - dist[d[i]]
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
