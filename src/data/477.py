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

que = deque()
que.append(0)
seen = [-1] * (n)
seen[0] = 0
par = [0] * (n)
child = [[] for _ in range(n)]
seq = []
while que:
    v = que.popleft()
    seq.append(v)
    for u in adj[v]:
        if seen[u] == -1:
            seen[u] = seen[v] + 1
            par[u] = v
            child[v].append(u)
            que.append(u)

for i in range(q):
    ans = seen[c[i]] - seen[d[i]]
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
