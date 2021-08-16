import math
import collections
import itertools
import copy
from collections import defaultdict, deque
import re
import heapq
from itertools import product
from functools import reduce
from operator import add, truediv
from operator import sub
from operator import mul
from heapq import heappush, heappop, heapify
import sys
import random
import bisect
from typing import List
import time
import random
#from scipy.sparse.csgraph import floyd_warshall  #呪文を唱える
#import numpy as np

sys.setrecursionlimit(10**7)  #再帰関数の呼び出し制限
INF = 10**30

MOD = 10**9 + 7

N, Q = (map(int, input().split()))

T = [[] for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    T[a].append([b, 1])
    T[b].append([a, 1])

d = [-1] * (N + 1)
q = deque([1])
d[1] = 0
while q:
    c = q.popleft()
    for i in T[c]:
        if d[i[0]] == -1:
            d[i[0]] = d[c] + i[1]
            q.append(i[0])
for _ in range(Q):
    x, y = map(int, input().split())
    if (d[x] + d[y]) % 2 == 0:
        print("Town")
    else:
        print("Road")
