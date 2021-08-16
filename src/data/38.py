import math
import itertools
import bisect
from heapq import heappush, heappop
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
road = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = IN()
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)

que = deque([])
que.append(0)

cnt = [0] * N
visited = [0] * N

while que:
    before = que.pop()
    if visited[before] == 1:
        continue
    visited[before] = 1

    for visit in road[before]:
        cnt[visit] = 1 - cnt[before]
        que.append(visit)

ans = [0] * Q
for k in range(Q):
    c, d = IN()
    if cnt[c - 1] == cnt[d - 1]:
        ans[k] = "Town"
    else:
        ans[k] = "Road"
print(*ans, sep="\n")
