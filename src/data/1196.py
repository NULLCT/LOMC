import math, itertools, fractions, heapq, collections, bisect, sys, queue, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def LS():
    return sys.stdin.readline().split()


def S():
    return input()


# dijkstra -- START --
def dijkstra(n, s, edge):
    d = [10**20] * n
    used = [False] * n
    d[s] = 0
    used[s] = True
    pq = []
    for e in edge[s]:
        heapq.heappush(pq, e)
    while pq:
        c, v = heapq.heappop(pq)
        if used[v]:
            continue
        d[v] = c
        used[v] = True
        for nc, nv in edge[v]:
            if not used[nv]:
                nd = nc + c
                if d[nv] > nd:
                    heapq.heappush(pq, [nd, nv])
    return d


# How to use -- START --
# Verify: https://atcoder.jp/contests/typical90/tasks/typical90_m
#
# edge=[[] for _ in range(n)]
# for _ in range(m):
#   x,y,cost=LI()
#   x-=1
#   y-=1
#   edge[x].append([cost,y])
#   edge[y].append([cost,x])
# st=0
# d=dijkstra(n,st,edge)
#
# How to use --- END ---
# dijkstra --- END ---

n, q = LI()
V = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = LI()
    a -= 1
    b -= 1
    V[a].append([1, b])
    V[b].append([1, a])

d = dijkstra(n, 0, V)
ans = []
for _ in range(q):
    c, dd = LI()
    c -= 1
    dd -= 1
    if abs(d[c] - d[dd]) % 2 == 0:
        ans.append('Town')
    else:
        ans.append('Road')

for x in ans:
    print(x)

# def main():

# main()
# print(main())
