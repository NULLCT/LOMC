from collections import deque

n, q = map(int, input().split())
L = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    L[a].append(b)
    L[b].append(a)

inf = 10**7
dist = [inf] * n

dq = deque()
dq.append(0)
dist[0] = 0
while dq:
    p = dq.popleft()
    for np in L[p]:
        if dist[np] == inf:
            dist[np] = dist[p] + 1
            dq.append(np)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    l = dist[c] + dist[d] - 2
    if l % 2 == 0:
        print('Town')
    else:
        print('Road')
