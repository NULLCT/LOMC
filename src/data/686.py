from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
r = [-1] * n
r[0] = 0
queue = deque()
queue.append(0)
while queue:
    x = queue.popleft()
    for y in graph[x]:
        if r[y] == -1:
            r[y] = r[x] ^ 1
            queue.append(y)
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if r[c] == r[d]:
        print('Town')
    else:
        print('Road')
