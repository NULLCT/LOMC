(N, _), *r = [map(int, s.split()) for s in open(0)]
G = [[] for _ in r + [7]]
for a, b in r[:N - 1]:
    G[a] += b,
    G[b] += a,
V = [1] * N + [0]
q = [N]
while q:
    i = q.pop()
    for j in G[i]:
        q += [j] * V[j]
        V[j] = ~V[i]
for c, d in r[N - 1:]:
    print('RTooawdn'[V[c] == V[d]::2])
