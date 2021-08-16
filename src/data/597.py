import sys
from collections import deque

sys.setrecursionlimit(10**7)


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return map(int, sys.stdin.readline().rstrip().split())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LI2():
    return list(map(int, sys.stdin.readline().rstrip()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def LS2():
    return list(sys.stdin.readline().rstrip())


N, Q = MI()
Graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = MI()
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)

dist = [-1] * N
deq = deque([0])
dist[0] = 0
while deq:
    i = deq.pop()
    for j in Graph[i]:
        if dist[j] == -1:
            dist[j] = 1 ^ dist[i]
            deq.append(j)

for _ in range(Q):
    c, d = MI()
    c -= 1
    d -= 1
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
