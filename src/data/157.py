from collections import deque

n, q = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1] += [b - 1]
    g[b - 1] += [a - 1]

visited = [-1] * n
deq = deque([0])
visited[0] = 0

while deq:
    v = deq.pop()
    for nv in g[v]:
        if visited[nv] != -1:
            continue
        visited[nv] = visited[v] ^ 1
        deq.append(nv)

for _ in range(q):
    c, d = map(int, input().split())
    if visited[c - 1] == visited[d - 1]:
        print('Town')
    else:
        print('Road')