import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import random
import re
import sys
import time
import string
from typing import List

sys.setrecursionlimit(99999)

n, q = map(int, input().split())
g = collections.defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

used = [0] * (n + 1)
depth = [0] * (n + 1)


def dfs(cur, dep):
    used[cur] = 1
    depth[cur] = dep
    for nc in g[cur]:
        if used[nc] == 0:
            dfs(nc, dep ^ 1)


dfs(1, 0)

for _ in range(q):
    m, n = map(int, input().split())
    if depth[m] != depth[n]:
        print("Road")
    else:
        print("Town")
