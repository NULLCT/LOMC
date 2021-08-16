#!python3.8
# -*- coding: utf-8 -*-
# abc209/d
import sys
import re
import math
from collections import *
from itertools import *
from decimal import *
from functools import *

from scipy.sparse import csgraph


def s2ss(s):
    return s.split()


def s2nn(s):
    return list(map(int, s2ss(s)))


def i2s():
    return sys.stdin.readline().rstrip()


def i2ss():
    return s2ss(i2s())


def i2n():
    return int(i2s())


def i2nn():
    return s2nn(i2s())


def debug(*arg):
    return print('DEBUG:', *arg) if sys.argv[1:] else None


import numpy as np
from scipy.sparse.csgraph import shortest_path, dijkstra
from scipy.sparse import csr_matrix

N, Q = i2nn()
n = 2 * (N - 1)
data = [1] * n
row = [None] * n
col = [None] * n
for i in range(0, n, 2):
    a, b = map(lambda x: x - 1, i2nn())
    row[i:i + 2] = [a, b]
    col[i:i + 2] = [b, a]
csr = csr_matrix((data, (row, col)), shape=(N, N), dtype=np.int32)
path = dijkstra(csr, directed=False, indices=0, unweighted=True)
#print(path)
#exit()
for i in range(Q):
    c, d = map(lambda x: x - 1, i2nn())
    x = path[c]
    y = path[d]
    if x % 2 != y % 2:
        print('Road')
    else:
        print('Town')
