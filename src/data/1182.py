n, q = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
inf = 10**10
d = [inf] * n
from collections import deque

Q = deque()
Q.append(0)
d[0] = 0
while Q:
    pos = Q.popleft()
    for i in G[pos]:
        if d[i] == inf:
            d[i] = d[pos] + 1
            Q.append(i)

for _ in range(q):
    s, t = map(int, input().split())
    if d[s - 1] % 2 == d[t - 1] % 2:
        print('Town')
    else:
        print('Road')
