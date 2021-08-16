import sys

sys.setrecursionlimit(10**9)
n, q = map(int, input().split())
ablist = [list(map(int, input().split())) for i in range(n - 1)]
cdlist = [list(map(int, input().split())) for i in range(q)]

graph = [list() for i in range(n)]
for a, b in ablist:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

edge_i = 0
for i, t in enumerate(graph):
    if len(t) == 1:
        edge_i = i
        break

distl = [-1] * n


def dist(n, d):
    distl[n] = d
    for t in graph[n]:
        if distl[t] != -1:
            continue
        dist(t, d + 1)


dist(edge_i, 0)

for c, d in cdlist:
    if abs(distl[c - 1] - distl[d - 1]) % 2 == 0:
        print("Town")
    else:
        print('Road')
