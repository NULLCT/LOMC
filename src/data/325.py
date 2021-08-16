# BFS
# DFS
import sys

sys.setrecursionlimit(20000000)
n, q = map(int, input().split())
a = [[] for i in range(n - 1)]
b = [[] for i in range(n - 1)]
c = [0] * q
d = [0] * q
g = [[] for i in range(n)]

for i in range(n - 1):
    a[i], b[i] = map(int, input().split())
    g[a[i] - 1].append(b[i] - 1)
    g[b[i] - 1].append(a[i] - 1)
for i in range(q):
    c[i], d[i] = map(int, input().split())

seen = [False for i in range(n)]
color = [-1 for i in range(n)]


def BFS(g, start):
    seen[start] = True

    for i in g[start]:
        if (seen[i] == False):
            seen[i] = True
            color[i] = 1 - color[start]
            BFS(g, i)


color[0] = 0
BFS(g, 0)

for i in range(q):
    if (color[c[i] - 1] == color[d[i] - 1]):
        print('Town')
    else:
        print('Road')
