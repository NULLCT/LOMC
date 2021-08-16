def LI():
    return list(map(int, input().split()))


from collections import deque

N, Q = LI()

START = 1

Past = [[] for i in range(N + 1)]
Fixed = [False for i in range(N + 1)]
Deep = [0 for i in range(N + 1)]
for i in range(N - 1):
    A, B = LI()
    Past[A].append(B)
    Past[B].append(A)

bits = 0
while (1 << bits) < N:
    bits += 1
par = [[0 for _ in range(N + 1)] for i in range(bits + 1)]

q = deque()
q.append(START)  #探索の初期値：スタートの値代入
Fixed[START] = True
Deep[START] = 1
while q:
    st = q.popleft()
    for to in Past[st]:
        if Fixed[to]:
            continue
        Fixed[to] = True
        Deep[to] = Deep[st] + 1
        par[0][to] = st
        q.append(to)

for k in range(bits):
    for v in range(1, N + 1):
        par[k + 1][v] = par[k][par[k][v]]


def lca(a, b):
    if a == b:
        return a
    if Deep[a] < Deep[b]:
        K = Deep[b] - Deep[a]
        for i in range(bits + 1):
            if (K >> i) & 1 == 1:
                b = par[i][b]
    if Deep[a] > Deep[b]:
        K = Deep[a] - Deep[b]
        for i in range(bits + 1):
            if (K >> i) & 1 == 1:
                a = par[i][a]
    if a == b:
        return a

    for i in range(bits, -1, -1):
        if par[i][a] != par[i][b]:
            a = par[i][a]
            b = par[i][b]

    return par[0][a]


for q in range(Q):
    c, d = LI()
    LCA = lca(c, d)
    path = Deep[c] + Deep[d] - 2 * Deep[LCA]
    if path % 2 == 0:
        print("Town")
    else:
        print("Road")
