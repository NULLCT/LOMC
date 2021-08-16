import sys
from collections import deque, defaultdict, Counter
from copy import deepcopy
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate
from functools import reduce
from math import gcd, sin, cos, tan, asin, acos, atan, degrees, radians, ceil, floor, log, sqrt, ceil, floor, pi, hypot
from string import ascii_lowercase
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

sys.setrecursionlimit(1000000)
INF = 10**18
MOD = 10**9 + 7
# MOD = 998244353
yes = "Yes"
no = "No"
from random import randint


def II():
    return int(input())


def SI():
    return str(input())


def MI():
    return map(int, input().split())


def MS():
    return map(str, input().split())


def LI():
    return list(map(int, input().split()))


def SLI():
    return sorted(list(map(int, input().split())))


N, Q = map(int, input().split())
L = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)
P = [0] * (N + 1)
T = [0] * (N + 1)


def dfs(p, cnt):
    P[p] = cnt
    T[p] = 1
    for l in L[p]:
        if T[l] == 0:
            dfs(l, cnt + 1)


dfs(1, 0)
for i in range(Q):
    a, b = map(int, input().split())
    if (P[a] + P[b]) % 2 == 0:
        print('Town')
    else:
        print('Road')
