from collections import deque

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]

color = [-1 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

q = deque()

color[0] = 0
q.append(0)

while len(q) > 0:
    node = q.popleft()
    for nx in edge[node]:
        if color[nx] < 0:
            color[nx] = (color[node] + 1) % 2
            q.append(nx)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')
