import sys
import bisect
from collections import deque
import itertools
import math

# sys.setrecursionlimit(10**4)
from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10**18
mod = 10**9 + 7
# mod = 998244353

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson

if __name__ == '__main__':
    n, q = lr()
    e = [lr() for i in range(n - 1)]
    m = n - 1
    edge = np.array(e, dtype=np.int64).T
    tmp = np.ones(m, dtype=np.int64).T
    graph = csr_matrix((tmp, (edge[:] - 1)), (n, n))
    dist = shortest_path(graph, indices=0, method='D', directed=False)

    for _ in range(q):
        c, d = lr()
        c -= 1
        d -= 1
        if (dist[c] - dist[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")
