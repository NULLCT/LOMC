from collections import deque
import time

N, Q = map(int, input().split())
graph = {}
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph.setdefault(a, [])
    graph.setdefault(b, [])
    graph[a].append(b)
    graph[b].append(a)

array = [-1] * N
d = deque()
d.append((0, 0))

while len(d):
    v, distance = d.popleft()
    array[v] = distance
    for w in graph.get(v, []):
        if array[w] != -1:
            continue

        d.append((w, distance + 1))

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    if (array[c] - array[d]) % 2 != 0:
        print('Road')
    else:
        print('Town')
