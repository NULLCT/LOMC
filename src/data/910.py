N, Q = map(int, input().split())
mich = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    mich[a - 1].append(b - 1)
    mich[b - 1].append(a - 1)
from collections import deque


def bfs(u):
    queue = deque([u])
    d = [None] * N
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in mich[v]:
            if d[i] == None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


kyo = bfs(0)
for i in range(Q):
    c, e = map(int, input().split())
    a = kyo[c - 1]
    b = kyo[e - 1]
    if (a - b) % 2 == 1:
        print("Road")
    else:
        print("Town")
