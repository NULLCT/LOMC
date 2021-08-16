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


deep = [[] for i in range(n)]


def BFS_2(g, start):
    seen[start] = True

    for i in g[start]:
        if (seen[i] == False):
            seen[i] = True
            deep[i] = deep[start] + 1
            BFS_2(g, i)


color[0] = 0
deep[0] = 0
BFS_2(g, 0)

for i in range(q):
    if ((deep[c[i] - 1] + deep[d[i] - 1]) % 2 == 0):
        print('Town')
    else:
        print('Road')
