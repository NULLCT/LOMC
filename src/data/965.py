import sys
from collections import deque

n, q = map(int, input().split())

depth = [-1] * n
depth[0] = 0
edge = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

stack = deque([0])

while stack:
    at = stack.popleft()
    d = depth[at]
    for town in edge[at]:
        if depth[town] == -1:
            stack.append(town)
            depth[town] = d + 1

for i in range(q):
    c, d = map(int, input().split())
    if (depth[c - 1] + depth[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
