#!/usr/bin/env python3

N, Q = map(int, input().split())
M = []
for i in range(N):
    M.append([])
for i in range(N - 1):
    a, b = map(int, input().split())
    M[a - 1].append(b - 1)
    M[b - 1].append(a - 1)
D = [0] * N
next = [0]
added = set()
added.add(0)
L = 0
while len(next) > 0:
    nnext = []
    L += 1
    while len(next) > 0:
        p = next.pop()
        for pc in M[p]:
            if pc not in added:
                nnext.append(pc)
                added.add(pc)
        D[p] = L
    next = nnext

for i in range(Q):
    s, t = map(int, input().split())
    dd = abs(D[s - 1] - D[t - 1])
    print("Road" if dd % 2 == 1 else "Town")
