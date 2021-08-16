N, Q = map(int, input().split())
E = {n: [] for n in range(1, 1 + N)}
for i in range(1, N):
    a, b = map(int, input().split())
    E[a] += [b]
    E[b] += [a]  #only forwarding

D = {}  # id, even(i.e. 0) or odd(i.e. 1)
c = 1
for d in range(1, N + 1):
    P = [(c, 0)]
    while P:
        p, path = P.pop(0)  # BFS
        if p in D: continue
        D[p] = path
        for dest in E[p]:
            if dest not in D: P += [(dest, path + 1)]

for i in range(1, Q + 1):
    c, d = map(int, input().split())
    if D[c] % 2 == D[d] % 2: print('Town')
    else: print('Road')
