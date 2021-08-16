# -*- coding: utf-8 -*-
import math
import collections
import bisect
import itertools
import heapq
import os
from collections import defaultdict, deque, Counter
import sys
import copy
import string
from pprint import pprint
from decimal import Decimal
import re

sys.setrecursionlimit(10**9)
readline = sys.stdin.readline
INF = float("INF")


def read_ints():
    return map(lambda x: int(x), readline().split())


def read_int():
    return int(readline())


def read_int_array():
    return list(read_ints())


def read_str():
    return readline().rstrip(os.linesep)


def read_str_array(size):
    return [read_str() for _ in [0] * size]


def read_int_arrays(size):
    return [read_int_array() for _ in [0] * size]


N, Q = read_ints()

connect = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = read_ints()
    connect[a - 1].append(b - 1)
    connect[b - 1].append(a - 1)

dists = [0] * N
D = 0

yet = [True] * N  # 無向グラフの場合、子から親に戻らないようにするのに必要
parents = [0]
yet[0] = False
while parents:
    next_parents = []
    for parent in parents:
        dists[parent] = D
        children = connect[parent]
        for child in children:
            if yet[child]:
                next_parents.append(child)
                yet[child] = False
    parents = next_parents
    D += 1

for _ in range(Q):
    c, d = read_ints()
    c_dist = dists[c - 1]
    d_dist = dists[d - 1]
    if (c_dist - d_dist) % 2 == 0:
        print("Town")
    else:
        print("Road")
