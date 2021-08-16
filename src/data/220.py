# -*- coding: utf-8 -*-
from collections import deque

N, Q = map(int, input().split())

D = dict()
for i in range(N):
    D[i] = []

for i in range(N - 1):
    A, B = map(int, input().split())
    D[A - 1].append(B - 1)
    D[B - 1].append(A - 1)

X = [0] * N

q = deque([0])
X[0] = 1

while (q):
    i = q.popleft()
    for j in D[i]:
        if X[j] == 0:
            X[j] = X[i] * -1
            q.append(j)

for i in range(Q):
    C, D = map(int, input().split())
    if X[C - 1] * X[D - 1] < 0:
        print("Road")
    else:
        print("Town")
