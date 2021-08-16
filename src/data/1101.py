import heapq

#ちょっとでもinputを速く
import sys

input = sys.stdin.readline

#再帰上限回数をすごくふやすよ　でもpythonであんまり再帰したくないね……
import sys
import resource

sys.setrecursionlimit(1000000)

n, q = map(int, input().split())

roads = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    roads[a - 1].append(b - 1)
    roads[b - 1].append(a - 1)

visited = [False for _ in range(n)]
dist = [0] * n


def visit(start):
    hq = [(start, 0)]
    heapq.heapify(hq)
    while hq:
        point, dis = heapq.heappop(hq)
        dist[point] = dis
        visited[point] = True
        for w in roads[point]:
            if not visited[w]:
                heapq.heappush(hq, (w, dis + 1))


visit(0)
for _ in range(q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2:
        print('Road')
    else:
        print('Town')
