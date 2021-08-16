N, Query = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
depth = [-1] * N
depth[0] = 0
Q = [0]
while Q:
    at = Q.pop()
    for n in G[at]:
        if depth[n] >= 0:
            continue
        depth[n] = depth[at] + 1
        Q.append(n)
#print(depth)
for _ in range(Query):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (depth[c] + depth[d]) % 2:
        print('Road')
    else:
        print('Town')
