R = lambda: map(int, input().split())
n, q = R()
g = [None] + [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = R()
    g[b].append(a)
    g[a].append(b)
C = [None] * (n + 1)
C[1] = 0
s = [1]
while s:
    u = s.pop()
    for v in g[u]:
        if C[v] is None:
            s.append(v)
            C[v] = C[u] ^ 1
for _ in range(q):
    c, d = R()
    print('TRoowand'[C[c] ^ C[d]::2])
