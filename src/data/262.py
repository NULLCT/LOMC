N, Q = map(int, input().split())
g = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
query = []
for i in range(Q):
    c, d = map(int, input().split())
    query.append((c - 1, d - 1))
oe = [0] * N
from collections import deque

q = deque([])
q.append((0, 0))
done = [0] * N
while q:
    now, count = q.popleft()
    if not done[now]:
        done[now] = 1
        oe[now] = count
        for nv in g[now]:
            if not done[nv]:
                q.append((nv, (count + 1) % 2))

for c, d in query:
    if oe[c] + oe[d] == 1:
        print('Road')
    else:
        print('Town')
