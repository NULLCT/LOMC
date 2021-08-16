N, Q = map(int, input().split())

edge = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

color = [-1] * N

qu = [(0, 0)]

while qu:
    i, c = qu.pop()
    if color[i] == -1:
        color[i] = c
        for nxt in edge[i]:
            qu.append((nxt, 1 if c == 0 else 0))

for q in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
