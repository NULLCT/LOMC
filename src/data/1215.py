import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().rstrip().split())
V = [0] * N
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

q = deque()

q.append(0)
V[0] = 1
while q:
    u = q.popleft()
    if V[u] == 1:
        state = 2
    else:
        state = 1

    for v in E[u]:
        if V[v] == 0:
            V[v] = state
            q.append(v)

for q in range(Q):
    c, d = map(int, sys.stdin.readline().rstrip().split())
    if V[c - 1] == V[d - 1]:
        print("Town")
    else:
        print("Road")
