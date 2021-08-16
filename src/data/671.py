N, Q = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

D = [None] * N
d = 0
to = {0}
while to:
    next_to = set()
    for v in to:
        D[v] = d
        for u in G[v]:
            if D[u] == None:
                next_to.add(u)
    to = next_to
    d += 1

for _ in range(Q):
    c, d = list(map(lambda x: int(x) - 1, input().split()))
    if (D[c] - D[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
