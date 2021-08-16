import math
from collections import deque, Counter
from itertools import product, combinations, permutations

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]

g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = ab[i][0], ab[i][1]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dist = [-1] * n
godeq = deque()
root = 0

dist[root] = 0
godeq.append(root)

while (godeq):
    v = godeq.popleft()
    for next in g[v]:
        if dist[next] != -1:
            continue
        else:
            dist[next] = dist[v] + 1
            godeq.append(next)

for qu in cd:
    if (dist[qu[1] - 1] - dist[qu[0] - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
