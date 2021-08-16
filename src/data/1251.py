from collections import defaultdict, deque
from itertools import permutations, combinations, product
from functools import lru_cache


def pprint(E):
    for e in E:
        print(e)


from sys import setrecursionlimit, stdin

setrecursionlimit(500000)
readline = stdin.readline
# @lru_cache(maxsize=None)
INF = 10**18
MOD = 1000000007
MOD2 = 998244353
cnt = ans = tmp = 0
yes, no = 'Yes', 'No'
yn = yes


def I():
    return int(readline())


def S():
    return readline()[:-1]


def LI():
    return list(map(int, readline().split()))


def SPI():
    return map(int, readline().split())


def FIE(x):
    return [readline()[:-1] for _ in [0] * x]


def ENU(x):
    return enumerate(x)


def NODE(x):
    return [[] for _ in [0] * (x + 1)]


def ZERO(x):
    return [0] * x


def ZEROS(y, x):
    return [[0] * x for _ in [0] * y]


def ZEROSS(z, y, x):
    return [[[0] * x for _ in [0] * y] for _ in [0] * z]


####################################################################
n, q = SPI()
node = NODE(n + 1)
for _ in range(n - 1):
    a, b = SPI()
    node[a].append((b, 1))
    node[b].append((a, 1))

from heapq import heappush, heappop

dist, done = [INF] * (n + 1), [0] * (n + 1)
hq = [(0, 1)]  # (cost, node)
dist[1] = 0
while hq:
    v = heappop(hq)[1]  # get a node
    done[v] = 1
    for to, cost in node[v]:
        if done[to] == 0 and dist[v] + cost < dist[to]:
            dist[to] = dist[v] + cost
            heappush(hq, (dist[to], to))

for _ in range(q):
    c, d = SPI()
    tmp = dist[c] + dist[d]
    if tmp % 2 == 0: print('Town')
    else: print('Road')
