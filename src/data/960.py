import collections
from collections import deque

n, q = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n - 1)]
a, b = [list(i) for i in zip(*ab)]
cd = [map(int, input().split()) for _ in range(q)]
c, d = [list(i) for i in zip(*cd)]

g = collections.defaultdict(list)
for frm, to in zip(a, b):
    g[frm].append(to)
    g[to].append(frm)

queue = deque()
visited = [0 for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
queue.append(1)
ansz = [1]
# ansz2 = []
before = 0
while len(queue) > 0:
    target = queue.popleft()
    if visited[target] == 1:
        continue
    visited[target] = 1
    for node in g[target]:
        if visited[node] == 1:
            continue
        distance[node] = distance[target] + 1
        # if distance[node] % 2 == 0:
        # ansz.append(node)
        # else:
        # ansz2.append(node)
        queue.append(node)

# print(distance)
for i in range(q):
    if (distance[c[i]] - distance[d[i]]) % 2 == 0:
        print("Town")
    else:
        print("Road")
