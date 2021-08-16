# D - Collision
from collections import defaultdict
from collections import deque

N, Q = map(int, input().split())
edges = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

dep = [-1] * (N + 1)
seen = [False] * (N + 1)

que = deque()
que.append((1, 0))

while len(que) > 0:
    v, d = que.pop()

    if not seen[v]:
        dep[v] = d
        seen[v] = True

        for e in edges[v]:
            que.append((e, d + 1))

for _ in range(Q):
    c, d = map(int, input().split())

    if (dep[c] + dep[d]) % 2 == 1:
        print('Road')
    else:
        print('Town')
