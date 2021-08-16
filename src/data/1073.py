from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from decimal import Decimal
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, combinations_with_replacement, product
from math import gcd, factorial, log2, ceil, floor, sin, asin, cos, acos, tan, atan, degrees
from pprint import pprint
from random import randrange
from sys import setrecursionlimit
from time import time

setrecursionlimit(10**9)
MOD = 10**9 + 7
INF = 10**18

N, Q = map(int, input().split())
#道の数のメモを作る？
#1からの距離を覚えておいてそれの差でいいんじゃないの？
road = [[] for _ in range(N)]
for n in range(N - 1):
    A, B = map(int, input().split())
    road[A - 1].append(B - 1)
    road[B - 1].append(A - 1)
dist = 0
dist_from0 = [0] * N
visited = [0] * N
visited[0] = 1


def dfs(now):
    global dist
    dist += 1
    dist_from0[now] = dist
    for next_town in road[now]:
        if visited[next_town] == 0:
            visited[next_town] = 1
            dfs(next_town)
    dist -= 1


dfs(0)
for q in range(Q):
    C, D = map(int, input().split())
    if abs(dist_from0[C - 1] - dist_from0[D - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
