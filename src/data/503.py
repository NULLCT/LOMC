import math
import itertools
import bisect
import heapq
from sys import stdin
from collections import deque
from sys import setrecursionlimit
from functools import reduce
from collections import defaultdict

setrecursionlimit(10**7)
input = stdin.readline


def I():
    return int(input())


def IN():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


def LIN():
    return [list(map(int, input().split())) for _ in range(N)]


N, Q = IN()
m = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = IN()
    a -= 1
    b -= 1
    m[a].append(b)
    m[b].append(a)

p = [-1] * N
p[0] = 0
que = deque()
que.append(0)
while que:
    j = que.popleft()

    for k in m[j]:
        if p[k] == -1:
            p[k] = 1 - p[j]
            que.append(k)
for j in range(Q):
    c, d = IN()
    if p[c - 1] == p[d - 1]:
        print("Town")
    else:
        print("Road")
