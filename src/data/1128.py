n, q = map(int, input().split())
ab = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)

inf = 10**15
from collections import deque

que = deque()
visited = [0] * n
dist = [inf] * n
que.append(0)
visited[0] = 1
dist[0] = 0

while que:
    x = que.popleft()
    for i in ab[x]:
        if dist[i] > dist[x] + 1 and visited[i] == 0:
            dist[i] = dist[x] + 1
            visited[i] = 1
            que.append(i)
#print(dist)
for i in range(q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
