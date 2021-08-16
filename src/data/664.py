from collections import deque

n, q, *abcd = map(int, open(0).read().split())
ab = abcd[:n * 2 - 2]
cd = abcd[n * 2 - 2:]
g = [[] for i in range(n + 1)]
for i in range(0, len(ab), 2):
    a = ab[i]
    b = ab[i + 1]
    g[a].append(b)
    g[b].append(a)

q = deque([(1, 0)])
dists = [-1] * (n + 1)
while q:
    v, n = q.popleft()
    dists[v] = n
    n += 1
    for x in g[v]:
        if dists[x] != -1: continue
        q.append((x, n))

for i in range(0, len(cd), 2):
    c = cd[i]
    d = cd[i + 1]
    if dists[c] % 2 == dists[d] % 2:
        print('Town')
    else:
        print('Road')
