import sys

input = sys.stdin.readline
from collections import deque

n, Q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dist = [0] * n
q = deque([(0, 0, -1)])
while q:
    step, i, par = q.popleft()
    for j in G[i]:
        if j == par: continue
        dist[j] = step + 1
        q.append((step + 1, j, i))
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2:
        print("Road")
    else:
        print("Town")
