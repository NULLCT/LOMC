n, q = map(int, input().split())
k = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    k[a - 1].append(b - 1)
    k[b - 1].append(a - 1)
from collections import deque

x = [-1] * n
x[0] = 0
d = deque()
d.append(0)
visit = [1] * n
visit[0] = 0
while d:
    g = d.popleft()
    for i in k[g]:
        if visit[i]:
            d.append(i)
            visit[i] = 0
            if x[g] == 0:
                x[i] = 1
            elif x[g] == 1:
                x[i] = 0
for i in range(q):
    c, d = map(int, input().split())
    if x[c - 1] == x[d - 1]:
        print('Town')
    else:
        print('Road')
