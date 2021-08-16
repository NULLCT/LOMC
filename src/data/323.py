(n, q), *t = [map(int, t.split()) for t in open(0)]
e = [[] for _ in t + t]
for a, b in t[:n - 1]:
    e[a] += b,
    e[b] += a,
d = [1] * n + [0]
q = [n]
for v in q:
    for w in e[v]:
        q += [w] * d[w]
        d[w] = ~d[v]
for a, b in t[n - 1:]:
    print('RTooawdn'[d[a] == d[b]::2])
