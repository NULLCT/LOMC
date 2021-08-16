import heapq
import sys

sys.setrecursionlimit(3000000)

n, q = map(int, input().split())

g = [[] for _ in range(n + 1)]

color = ["x"] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# for i in range(1,n+1):
#     g[i].sort()


def bfs(start, bef, dim):

    if dim % 2 == 0:
        color[start] = "○"
    else:
        color[start] = "x"
    dim += 1
    for s in g[start]:
        if s != bef:
            bfs(s, start, dim)

    dim -= 1


dim = 1
bfs(1, -1, dim)

for i in range(q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
