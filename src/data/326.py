(n, q), *t = [map(int, t.split()) for t in open(0)]
*e, = eval('[],' * -~n)
for a, b in t[:n - 1]:
    e[a] += b,
    e[b] += a,
d = [0, 0] + [-1] * n
q = [1]
for v in q:
    for w in e[v]:
        if d[w] < 0:
            d[w] = d[v] + 1
            q += w,
for a, b in t[n - 1:]:
    print('TRoowand'[d[a] - d[b] & 1::2])
