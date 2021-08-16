n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
from collections import deque

d = deque()
d.append(0)
l = [-1] * n
l[0] = 0
while d:
    now = d.popleft()
    for i in g[now]:
        if l[i] == -1:
            d.append(i)
            l[i] = 1 - l[now]
for i in range(q):
    c, d = map(int, input().split())
    if l[c - 1] == l[d - 1]:
        print("Town")
    else:
        print("Road")
# print(l)
# print(g)
