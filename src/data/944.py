from collections import deque

n, q = map(int, input().split())
dist = [-1] * n
que = deque()
que.append(0)
dist[0] = 0
l = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    l[a - 1].append(b - 1)
    l[b - 1].append(a - 1)
while que:
    v = que.popleft()
    d = dist[v]
    for w in l[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)
for _ in range(q):
    c, d = map(int, input().split())
    k = abs(dist[c - 1] - dist[d - 1])
    if k % 2 == 0:
        print('Town')
    else:
        print('Road')
