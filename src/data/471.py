N, Q = map(int, input().split())
path = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)

dist = [-1] * N
v = [0]
while v:
    tmp = []
    for i in v:
        for j in path[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                tmp.append(j)
    v = tmp

for i in range(Q):
    c1, d1 = map(int, input().split())
    c1, d1 = c1 - 1, d1 - 1
    if abs(dist[c1] - dist[d1]) % 2:
        print('Road')
    else:
        print('Town')
