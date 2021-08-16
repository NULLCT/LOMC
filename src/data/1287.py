import sys
import math
from collections import deque, Counter
#sys.setrecursionlimit(10**7)
int1 = lambda x: int(x) - 1

mi = lambda: map(int, input().split())
li = lambda: list(mi())
mi1 = lambda: map(int1, input().split())
li1 = lambda: list(mi1())
mis = lambda: map(str, input().split())
lis = lambda: list(mis())

from collections import defaultdict
"""
d=defaultdict(int) #初期値 0
d=defaultdict(lambda:1) #初期値 1
"""

mod = 10**9 + 7
Mod = 998244353
INF = 10**18
ans = 0

d = deque()
n, q = mi()
# edge:辺
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
d.append(0)
depth = [-1] * n
depth[0] = 0
while d:
    x = d.pop()
    for i in edge[x]:
        if depth[i] == -1:
            depth[i] = depth[x] + 1
            d.append(i)
for i in range(q):
    c, d = mi1()
    s = depth[c] + depth[d]
    if s % 2 == 0:
        print('Town')
    else:
        print('Road')
