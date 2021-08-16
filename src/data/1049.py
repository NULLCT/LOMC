import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from collections import Counter
from collections import defaultdict as dd
from collections import deque

# sys.setrecursionlimit(100000000)

flush = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr = lambda x: stdout.write(str(x))
stdmap = lambda: map(int, stdstr().split())
stdarr = lambda: list(map(int, stdstr().split()))

mod = 1000000007


def BFS(node, graph):
    global n
    visited = [False] * (n + 1)

    distance = [0] * (n + 1)

    q = deque([node])

    while (q):
        curr = q.popleft()
        visited[curr] = True

        for i in graph[curr]:
            if (not visited[i]):
                distance[i] = distance[curr] + 1
                q.append(i)

    return distance


n, q = stdmap()

graph = dd(list)

for i in range(n - 1):
    a, b = stdmap()

    graph[a].append(b)
    graph[b].append(a)

dx = BFS(1, graph)

for _ in range(q):
    c, d = stdmap()

    diff = abs(dx[c] - dx[d])

    if (diff % 2 == 0):
        print("Town")
    else:
        print("Road")
