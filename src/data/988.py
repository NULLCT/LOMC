n, q = map(int, input().split())

p = [0] * n
d = dict()
for i in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]
    if b in d:
        d[b].append(a)
    else:
        d[b] = [a]

v = []
rp = 0
p[0] = 1
v.append(0)
while len(v) > rp:
    a = v[rp]
    rp += 1
    for b in d[a]:
        if p[b] == 0:
            p[b] = -p[a]
            v.append(b)

for i in range(q):
    c, d = [int(x) - 1 for x in input().split()]
    if p[c] == p[d]:
        print('Town')
    else:
        print('Road')
