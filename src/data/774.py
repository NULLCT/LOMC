import sys
import math
import itertools
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
from operator import itemgetter, attrgetter

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def RD():
    return input().rstrip()


def F():
    return float(input().rstrip())


def I():
    return int(input().rstrip())


def MI():
    return map(int, input().split())


def MF():
    return map(float, input().split())


def LI():
    return list(map(int, input().split()))


def TI():
    return tuple(map(int, input().split()))


def LF():
    return list(map(float, input().split()))


def Init(H, W, num):
    return [[num for i in range(W)] for j in range(H)]


def TL(mylist):
    return [list(x) for x in zip(*mylist)]  #行と列入れ替え


def RtoL(mylist):
    return [list(reversed(x)) for x in mylist]  #左右反転


def HtoL(mylist):
    return [x for x in list(reversed(mylist))]  #上下反転


def convert_2d(l, colstart, colend, rawstart, rawend):
    return [i[rawstart:rawend] for i in l[colstart:colend]]  #2次元行列から一部を採取


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


def main():
    N, Q = MI()
    G = [[] for i in range(N)]
    max_n = 1000000
    prv = []
    for i in range(N - 1):
        a, b = MI()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    dist = [-1 for i in range(N)]

    dq = deque()
    dq.append(0)
    dist[0] = 0
    while dq:
        v = dq.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                dq.append(nv)

    for i in range(Q):
        c, d = MI()
        c -= 1
        d -= 1
        if c > d:
            swap(c, d)
        if (dist[c] + dist[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
