import sys, math, heapq, bisect
from collections import defaultdict, deque

input = sys.stdin.readline

mod = (10**9) + 7

n, q = map(int, input().split())
G = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

vis = [-1] * (n + 1)
vis[1] = 0

Q = deque([1])

while (len(Q) != 0):
    a = Q.popleft()
    for b in G[a]:
        if (vis[b] == -1):
            vis[b] = vis[a] + 1
            Q.append(b)

for i in range(q):
    a, b = map(int, input().split())
    val = abs(vis[a] - vis[b])
    if (val % 2 != 0):
        print("Road")
    else:
        print("Town")
