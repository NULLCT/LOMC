N, Q = map(int, input().split())
E = {n + 1: [] for n in range(N)}
for i in range(1, N):
    a, b = map(int, input().split())
    E[a] += [b]
    E[b] += [a]
D, P = {1: 0}, [1]
while P:
    p = P.pop(0)
    for d in E[p]:
        if d in D: continue
        P += [d]
        D[d] = D[p] + 1
for _ in range(Q):
    c, d = map(int, input().split())
    print(D[c] % 2 == D[d] % 2 and 'Town' or 'Road')
