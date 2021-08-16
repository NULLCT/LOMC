import sys
from collections import deque

sys.setrecursionlimit(10**6)

N, Q = list(map(int, input().split()))
nodes = [[] for _ in range(N)]
child = [False] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    nodes[a - 1].append(b - 1)
    child[a - 1] = True
    nodes[b - 1].append(a - 1)
    child[b - 1] = True
parents = [0] * N
depths = [0] * N


def get_child(depth, now):
    if depths[now] != 0:
        return
    depths[now] = depth
    for i in range(len(nodes[now])):
        get_child(depth + 1, nodes[now][i])
        parents[nodes[now][i]] = now


def solve(child, nodes):
    for i in range(len(child)):
        if not child[i]:
            parent = i
            break
    get_child(0, parent)
    parents[parent] = -1


get_child(0, 0)
parents[0] = -1

for _ in range(Q):
    c, d = map(int, input().split())
    dist = abs(depths[c - 1] - depths[d - 1] + 1)
    if dist % 2 == 0:
        print("Road")
    else:
        print("Town")
# print(depths)
