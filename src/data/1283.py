import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product


def input():
    return sys.stdin.readline()[:-1]


def ruiseki(lst):
    return [0] + list(accumulate(lst))


def ceil(a, b):
    return -(-a // b)


def create_graph(N, edge):
    g = [[] for i in range(N)]
    for i, j in edge:
        i, j = i - 1, j - 1
        g[i].append(j)
        g[j].append(i)
    return g


sys.setrecursionlimit(5000000)
mod = pow(10, 9) + 7
INF = 1 << 100
al = [chr(ord('a') + i) for i in range(26)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n - 1)]
cd = [list(map(int, input().split())) for i in range(q)]

g = create_graph(n, ab)

# print(g)


# O(E+Vlog(V))
def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq)  # リストを優先度付きキューに変換
    cost = [float('inf')] * n  # 行ったことのないところはinf
    cost[s] = 0  # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:  # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost


n, m = n, n - 1
e = [[] for _ in range(n)]
for _ in range(m):
    a, b = ab[_]
    a, b = a - 1, b - 1
    e[a].append((1, b))
    e[b].append((1, a))

ans = 0
for i in range(n):
    if len(g[i]) == 1:
        ans = dijkstra(i)
        break
# print(ans)

for i in range(q):
    c, d = cd[i]
    c, d = c - 1, d - 1
    if abs(ans[c] - ans[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
