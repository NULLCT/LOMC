from sys import stdin
import sys

sys.setrecursionlimit(10**7)

n, q = map(int, stdin.readline().split())
edge = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    edge[a].append(b)
    edge[b].append(a)
colors = [0] * n


def dfs(v, color):
    #今いる点を着色
    colors[v] = color
    for to in edge[v]:
        if colors[to] == color:
            return False
        if colors[to] == 0 and not dfs(to, -color):
            return False
    return True


def is_bipartite():
    return dfs(0, 1)  # 頂点0を黒(1)で塗ってDFS開始


is_bipartite()

for _ in range(q):
    c, d = map(int, stdin.readline().split())
    s = colors[c - 1]
    t = colors[d - 1]

    if s == t:
        print('Town')
    else:
        print('Road')
