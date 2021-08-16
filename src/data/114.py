n, q = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
color = [None] * n
from collections import deque

dq = deque()
dq.append(0)
dist = [-1] * n
dist[0] = 1
while dq:
    now = dq.popleft()
    for next in tree[now]:
        if dist[next] != -1: continue
        dist[next] = dist[now] + 1
        dq.append(next)
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    c2 = dist[c] % 2
    d2 = dist[d] % 2
    if c2 ^ d2: print('Road')
    else: print('Town')
