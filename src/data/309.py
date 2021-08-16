from heapq import *
import sys
from collections import *
from itertools import *
from decimal import *
import copy
from bisect import *
import math

sys.setrecursionlimit(4100000)


def gcd(a, b):
    if (a % b == 0): return (b)
    return (gcd(b, a % b))


input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N - 1)]
cd = [list(map(int, input().split())) for i in range(Q)]

path = defaultdict(list)
for a, b in ab:
    path[a].append(b)
    path[b].append(a)

dp = [-1 for i in range(N + 1)]
dp[1] = 0

stack = [1]
while stack:
    c = stack.pop()
    count = dp[c]
    for a in path[c]:
        if dp[a] == -1:
            dp[a] = count + 1
            stack.append(a)

#print(dp)
for c, d in cd:
    if dp[c] % 2 == dp[d] % 2:
        print("Town")
    else:
        print("Road")
