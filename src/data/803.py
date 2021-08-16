import math
from collections import deque, Counter
from itertools import product, combinations, permutations

n, q = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n - 1)]
q = [list(map(int, input().split())) for _ in range(q)]

x = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = p[i][0], p[i][1]
    a -= 1
    b -= 1
    x[a].append(b)
    x[b].append(a)

dist = [-1] * n
G = deque()
root = 0
dist[root] = 0
G.append(root)
while (G):
    v = G.popleft()
    for next in x[v]:
        if dist[next] != -1:
            continue
        else:
            dist[next] = dist[v] + 1
            G.append(next)

for query in q:
    if (dist[query[1] - 1] - dist[query[0] - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
