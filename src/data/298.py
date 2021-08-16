n, q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n - 1)]
cd = [list(map(int, input().split())) for i in range(q)]
import sys

sys.setrecursionlimit(10**7)
from collections import defaultdict, deque

roads = defaultdict(list)
for a, b in ab:
    roads[a - 1].append(b - 1)
    roads[b - 1].append(a - 1)

color = [-1] * n

queue = deque()
queue.append((0, 0))
while len(queue) > 0:
    (node, depth) = queue.pop()
    color[node] = depth
    for i in roads[node]:
        if color[i] >= 0:
            continue
        queue.append((i, depth + 1))

for c, d in cd:
    c, d = c - 1, d - 1
    print("Road" if (color[c] + color[d]) % 2 else "Town")
