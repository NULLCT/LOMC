import math
# import numpy as np
import itertools
# import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
# from scipy.sparse.csgraph import dijkstra
# from scipy.sparse import csr_matrix
ipt = stdin.readline
# setrecursionlimit(10**7)
mod = 10**9 + 7
# mod = 998244353
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
alp = "abcdefghijklmnopqrstuvwxyz"
INF = 1 << 32 - 1
# INF = 10**18


def main():
    n, qs = map(int, ipt().split())
    wy = [[] for i in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, ipt().split())
        wy[a].append(b)
        wy[b].append(a)

    d = [-1] * (n + 1)

    q = [1]
    d[1] = 0
    while q:
        qi = q.pop()
        di = d[qi] + 1
        for ni in wy[qi]:
            if d[ni] == -1:
                d[ni] = di
                q.append(ni)

    for i in range(qs):
        c, di = map(int, ipt().split())
        xm = d[c] + d[di]
        if xm % 2:
            print("Road")
        else:
            print("Town")

    return None


if __name__ == '__main__':
    main()
