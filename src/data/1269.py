from collections import defaultdict as dd

N, Q = map(int, input().split())
Es = dd(dict)
for _ in range(N - 1):
    a, b = map(int, input().split())
    Es[a - 1][b - 1] = Es[b - 1][a - 1] = 1

q = [[0, 0]]
Xs = [None] * N
while q:
    node, x = q.pop()
    Xs[node] = x
    nx = (x + 1) % 2
    for to in Es[node].keys():
        if Xs[to] is not None: continue
        q.append([to, nx])

for _ in range(Q):
    c, d = map(int, input().split())
    if Xs[c - 1] == Xs[d - 1]:
        print('Town')
    else:
        print('Road')
