(N, _), *r = [map(int, s.split()) for s in open(0)]
G = [[] for _ in range(N + 1)]
for a, b in r[:N - 1]:
    G[a] += b,
    G[b] += a,
V = [1] * N + [0]
q = [N]
while q:
    i = q.pop()
    for j in G[i]:
        if V[j] > 0:
            V[j] = ~V[i]
            q += j,
for c, d in r[N - 1:]:
    print('RTooawdn'[V[c] == V[d]::2])
