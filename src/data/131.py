# 問題から結局ある一点からの距離を算出して、あるポイントからあるポイントまでの距離が
# 2で割れるかどうかを判定するだけだとわかる。
import sys

sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

roads = [[] for _ in range(N)]
dep = [0] * N
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    roads[a].append(b)
    roads[b].append(a)


# DFS
def dfs(x, last=-1):
    for to in roads[x]:
        if to == last:
            continue
        dep[to] = dep[x] + 1
        dfs(to, x)


dfs(0)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dep[c] % 2 == dep[d] % 2:
        print('Town')
    else:
        print('Road')
