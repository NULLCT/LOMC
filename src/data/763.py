import math

from collections import deque, Counter

from itertools import product, combinations, permutations

n, q = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(n - 1)]

cd = [list(map(int, input().split())) for _ in range(q)]

G = [[] for _ in range(n)]

for i in range(n - 1):

    a, b = ab[i][0], ab[i][1]

    a -= 1

    b -= 1

    G[a].append(b)

    G[b].append(a)

dist = [-1] * n

goto = deque()

root = 0

dist[root] = 0

goto.append(root)

while (goto):

    v = goto.popleft()

    for next in G[v]:

        if dist[next] != -1:

            continue

        else:

            dist[next] = dist[v] + 1

            goto.append(next)

for query in cd:

    if (dist[query[1] - 1] - dist[query[0] - 1]) % 2 == 0:

        print("Town")

    else:

        print("Road")
