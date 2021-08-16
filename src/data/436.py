import collections, math
from collections import defaultdict


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


from collections import deque, Counter
from collections import defaultdict
import itertools
import math
import heapq
import math

N, Q = MI()

#つながっている経路
road = [[] for i in range(N)]
for i in range(N - 1):
    a, b = MI()
    a -= 1
    b -= 1
    road[a].append(b)
    road[b].append(a)
"""
道路で出会うのはつながった街にいるとき
街で出会うのは、つながっている街の中継地点にいるとき

cとdの距離を事前に計算できていればよい
"""

#訪問フラグ兼距離
visit = [-1] * N
#BFSを解く
q = deque()
q.append(0)
visit[0] = 0

while q:
    pos = q.pop()
    #つながっている道に確認
    for nx in road[pos]:
        #未訪問なら訪問
        if visit[nx] == -1:
            #距離を追加
            visit[nx] = visit[pos] + 1
            q.append(nx)

#各距離の引き算を計算
ans = []
for i in range(Q):
    c, d = MI()
    c -= 1
    d -= 1
    dist = abs(visit[c] - visit[d])
    if dist % 2 == 0:
        ans.append("Town")
    else:
        ans.append("Road")

for i in ans:
    print(i)
