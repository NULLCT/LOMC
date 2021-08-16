from collections import deque

n, r = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
d = [-1] * n
q = deque([0])
while q:
    x = q.popleft()
    for i in g[x]:
        if d[i] == -1:
            d[i] = 1 - d[x]
            q.append(i)

for i in range(r):
    c, e = map(int, input().split())
    if d[c - 1] == d[e - 1]:
        print("Town")
    else:
        print("Road")
