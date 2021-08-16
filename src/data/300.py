import sys


def input():
    return sys.stdin.readline().strip()


def mapint():
    return list(map(int, input().split()))


sys.setrecursionlimit(10**9)

N, Q = mapint()
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = mapint()
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

from collections import deque

deq = deque()
deq.append((0, -1))
dist = [0] * N
while deq:
    v, par = deq.pop()
    for nv in graph[v]:
        if nv == par:
            continue
        dist[nv] = dist[v] + 1
        deq.append((nv, v))

for _ in range(Q):
    a, b = mapint()
    a, b = a - 1, b - 1
    if abs(dist[a] - dist[b]) % 2 == 1:
        print("Road")
    else:
        print("Town")
