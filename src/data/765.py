from collections import deque

N, Q = map(int, input().split())
D = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    D[a].append(b)
    D[b].append(a)

dist = [-1] * N
que = deque()
dist[0] = 0
que.append(0)

while que:
    v = que.popleft()

    for i in D[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        que.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    if (dist[c] + dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
