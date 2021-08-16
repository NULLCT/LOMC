n, q = map(int, input().split())

E, D = [[] for _ in range(-~n)], [0] * -~n
for i in range(n - 1):
    a, b = map(int, input().split())
    E[a] += [b]
    E[b] += [a]

L, p = [1], -1
while L:
    v = L.pop()
    d = D[v]
    for n in E[v]:
        if D[n] == 0:
            D[n] = -~d
            L += [n]

for i in range(q):
    c, d = map(int, input().split())
    print('Road' if abs(D[c] - D[d]) % 2 else 'Town')
