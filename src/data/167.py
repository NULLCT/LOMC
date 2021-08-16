from collections import deque
import numpy as np

n, q = map(int, input().split())
data = [[] for i in range(n)]

for i in range(n - 1):
    x, y = map(int, input().split())
    data[x - 1].append(y - 1)
    data[y - 1].append(x - 1)

color = [-1] * n
color[0] = 0
d = deque()
d.append(0)

while len(d) != 0:
    v = d.popleft()

    for z in data[v]:
        if color[z] == -1:
            d.append(z)
            color[z] = 1 - color[v]

for i in range(q):
    x, y = map(int, input().split())
    if color[x - 1] == color[y - 1]:
        print("Town")
    else:
        print("Road")
