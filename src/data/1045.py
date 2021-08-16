import sys

sys.setrecursionlimit(10**9)

n, q = map(int, input().split())
e = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

r = [-1 for _ in range(n)]
que = [(0, 0)]
while (que):
    qq = []
    for v, x in que:
        if r[v] != -1:
            continue
        r[v] = x
        for u in e[v]:
            if r[u] != -1:
                continue
            qq.append((u, x + 1))
    que = qq[:]

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if r[c] % 2 == r[d] % 2:
        print('Town')
    else:
        print('Road')
