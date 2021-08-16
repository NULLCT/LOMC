import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10**5))
INF = float("INF")
MOD = 10**9 + 7
import heapq
import math
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement, permutations
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edge[a].append(b)
    edge[b].append(a)

dist = [-1] * n
dist[0] = 0
que = deque()
que.append(0)

while que:
    x = que.popleft()
    for to in edge[x]:
        if dist[to] != -1:
            continue
        dist[to] = dist[x] + 1
        que.append(to)

for i in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
