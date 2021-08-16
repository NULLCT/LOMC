def inputlist():
    return list(map(int, input().split()))


def inputmap():
    return map(int, input().split())


def inputint():
    return int(input())


def inputstr():
    return str(input())


import sys
from collections import Counter
from collections import deque
import bisect
import itertools

sys.setrecursionlimit(10**6)

N, Q = inputmap()
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = inputmap()
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

que = deque()
que.append((0, 0))
depth_list = [-1] * N
while len(que) > 0:
    node, depth = que.pop()
    depth_list[node] = depth
    for child in graph[node]:
        if depth_list[child] != -1:
            continue
        que.append((child, depth + 1))

for i in range(Q):
    c, d = inputmap()
    if (depth_list[c - 1] - depth_list[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
