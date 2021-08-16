import bisect, collections, copy, heapq, itertools, math, string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return map(int, sys.stdin.readline().rstrip().split())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


from collections import deque, defaultdict, Counter
import heapq
from functools import reduce
from itertools import permutations
import math


def main():
    n, Q = MI()
    data = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = MI()
        data[a].append(b)
        data[b].append(a)
    double = [[-1 for _ in range(n + 1)] for _ in range(20)]
    dist = [-1] * (n + 1)
    dist[1] = 0
    oya = [-1] * (n + 1)
    oya[1] = 1
    q = deque()
    q.append(1)
    while q:
        now = q.pop()
        for to in data[now]:
            if dist[to] != -1:
                continue
            dist[to] = dist[now] + 1
            oya[to] = now
            q.append(to)
    for i in range(n + 1):
        double[0][i] = oya[i]
    for i in range(1, 20):
        for j in range(1, n + 1):
            pre = double[i - 1][j]
            double[i][j] = double[i - 1][pre]

    def LCA(a, b):
        if dist[a] == dist[b]:
            at = a
            bt = b
        else:
            sa = abs(dist[a] - dist[b])
            sa_bit = bin(sa)[2:]
            sa_bit = sa_bit[::-1]
            if dist[a] > dist[b]:
                at = a
                bt = b
                for i in range(len(sa_bit)):
                    if sa_bit[i] == "1":
                        at = double[i][at]
            else:
                at = a
                bt = b
                for i in range(len(sa_bit)):
                    if sa_bit[i] == "1":
                        bt = double[i][bt]
        if at == bt:
            return at
        for i in range(19, -1, -1):
            if double[i][at] == double[i][bt]:
                continue
            else:
                at = double[i][at]
                bt = double[i][bt]
        lca = oya[at]
        return lca

    for i in range(Q):
        c, d = MI()
        x = LCA(c, d)
        c_d_dist = dist[c] + dist[d] - (2 * dist[x])
        if c_d_dist % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == "__main__":
    main()
