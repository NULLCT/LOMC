import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext


# input = sys.stdin.readline
def i_input():
    return int(input())


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def i_row(N):
    return [i_input() for _ in range(N)]


def i_row_list(N):
    return [i_list() for _ in range(N)]


def s_input():
    return input()


def s_map():
    return input().split()


def s_list():
    return list(s_map())


def s_row(N):
    return [s_input for _ in range(N)]


def s_row_str(N):
    return [s_list() for _ in range(N)]


def s_row_list(N):
    return [list(s_input()) for _ in range(N)]


def lcm(a, b):
    return a * b // gcd(a, b)


sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 10**9 + 7
num_list = []
str_list = []

n, q = map(int, input().split())

inf = 10**6

road = [[] for i in range(n)]
dist = [inf for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)

C = []
D = []

for i in range(q):
    c, d = i_map()
    C.append(c - 1)
    D.append(d - 1)


def bfs():
    que = deque()
    que.append(0)
    dist[0] = 0

    while len(que) != 0:
        p = que.popleft()
        for i in road[p]:
            if dist[i] == inf:
                que.append(i)
                dist[i] = dist[p] + 1
    return


bfs()

for i in range(q):
    judge = (dist[C[i]] - dist[D[i]]) % 2
    if judge == 0:
        print('Town')
    else:
        print('Road')
