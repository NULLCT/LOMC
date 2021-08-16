from collections import deque

N, Q = map(int, input().split())
road = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    road[a].append(b)
    road[b].append(a)

dist = [-1] * N
dist[0] = 0
que = deque()
que.append(0)
while que:
    i = que.popleft()
    for j in road[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            que.append(j)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
