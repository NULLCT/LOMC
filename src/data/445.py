from collections import deque

n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    g[a].append(b)
    g[b].append(a)
dpt = list(-1 for i in range(n))
que = deque([0])
dpt[0] = 0
while que:
    u = que.popleft()
    for v in g[u]:
        if (dpt[v] == -1):
            dpt[v] = dpt[u] + 1
            que.append(v)
while q > 0:
    q = q - 1
    c, d = map(int, input().split())
    c = c - 1
    d = d - 1
    if (dpt[c] + dpt[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
