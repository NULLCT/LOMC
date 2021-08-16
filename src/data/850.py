from collections import deque

N, Q = map(int, input().split())

G = []
for _ in range(N):
    G.append([])

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = []
for _ in range(N):
    dist.append(-1)

que = deque()

que.append(0)
dist[0] = 0

while len(que) > 0:
    i = que.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            que.append(j)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    check = dist[c] - dist[d]
    if check % 2 == 0:
        print("Town")
    else:
        print("Road")
