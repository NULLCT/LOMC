(n, q), *t = [map(int, t.split()) for t in open(0)]
d = [1] * n + [0]
s = [n]
e = [[] for _ in d]
for a, b in t[:-q]:
    e[a] += b,
    e[b] += a,
for v in s:
    for w in e[v]:
        s += [w] * d[w]
        d[w] = ~d[v]
for a, b in t[-q:]:
    print('RTooawdn'[d[a] == d[b]::2])
