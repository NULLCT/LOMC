from collections import deque

n, q = map(int, input().split())
roads = [[] for _ in range(n)]
que = deque()

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    roads[a].append(b)
    roads[b].append(a)

dist = [-1] * n
que.append(0)
dist[0] = 0
while len(que) > 0:
    now = que.popleft()
    for i in roads[now]:
        if dist[i] != -1: continue
        dist[i] = dist[now] + 1
        que.append(i)

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
