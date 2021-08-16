N, Q = map(int, input().split())
E = {n: [] for n in range(1, 1 + N)}
for i in range(1, N):
    a, b = map(int, input().split())
    E[a] += [b]
    E[b] += [a]

D = {1: 0}
P = [1]
while P:
    p = P.pop(0)  # BFS
    for d in E[p]:
        if d in D: continue
        D[d] = D[p] + 1
        P += [d]

for _ in range(Q):
    c, d = map(int, input().split())
    print(D[c] % 2 == D[d] % 2 and 'Town' or 'Road')
