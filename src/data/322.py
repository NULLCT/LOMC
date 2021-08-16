(n, q), *t = [map(int, t.split()) for t in open(0)]
e = [[] for _ in t + t]
for a, b in t[:-q]:
    e[a] += b,
    e[b] += a,
d = [1] * n + [0]
s = [n]
for v in s:
    for w in e[v]:
        s += [w] * d[w]
        d[w] = ~d[v]
for a, b in t[-q:]:
    print('RTooawdn'[d[a] == d[b]::2])
