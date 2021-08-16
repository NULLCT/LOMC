def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7
#import numpy as np
import sys

sys.setrecursionlimit(2147483647)
import math
import bisect
import heapq
import re
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import Counter
from collections import deque
from collections import defaultdict
from decimal import Decimal

inf = float('inf')
dic = defaultdict(lambda: 0)

n, q = L()
ab = NL(n - 1)
cd = NL(q)

tree = [[] for i in range(n)]

for a, b in ab:
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

isVisit = [False] * n
q = deque([(0, 0)])
rank = [0] * n
i = 0
while q:
    now, dis = q.popleft()
    if isVisit[now]:
        continue
    isVisit[now] = True
    rank[now] = dis
    i += 1
    for to in tree[now]:
        q.append((to, dis + 1))

for c, d in cd:
    if (rank[c - 1] - rank[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
