# coding #

import math
import collections
import itertools
from collections import deque
import queue

# import numpy as np

import sys

sys.setrecursionlimit(10000)

n7 = 1000000007
res = float('inf')
ans = 0
flag = True

N, Q = list(map(int, input().split()))
G = [[] for i in range(N + 1)]

for i in range(N - 1):
    A, B = list(map(int, input().split()))
    G[A].append(B)
    G[B].append(A)

depth_vec = [-1 for _ in range(N + 1)]
q = deque()
q.append((1, 0))

while len(q) > 0:
    node, depth = q.pop()
    depth_vec[node] = depth
    for child in G[node]:
        if depth_vec[child] >= 0:
            continue
        q.append((child, depth + 1))

for query in range(Q):
    C, D = list(map(int, input().split()))
    if (depth_vec[C] + depth_vec[D]) % 2 == 0:
        print("Town")
    else:
        print("Road")
