#!/usr/bin/env python3

from functools import lru_cache
from heapq import heappush, heappop, heappushpop
from itertools import permutations
from operator import itemgetter
from collections import deque
from collections import Counter
from itertools import accumulate
from collections import defaultdict
import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl

sys.setrecursionlimit(2147483647)
mod = 10**9 + 7
inf = float('inf')


def I():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


n, q = LI()
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = LI()
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

D = [0] * n
checked = [False] * n
que = deque([(0, -1)])
checked[0] = True
while que:
    v, p = que.popleft()
    for u in edges[v]:
        if checked[u]:
            continue
        if u == p:
            continue
        checked[u] = True
        D[u] = D[v] + 1
        que.append((u, v))

for _ in range(q):
    c, d = LI()
    if (D[c - 1] + D[d - 1]) % 2:
        print("Road")
    else:
        print("Town")
