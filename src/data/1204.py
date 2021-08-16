N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N - 1)]
CD = [list(map(int, input().split())) for i in range(Q)]
c = [[] for i in range(N)]
for x, y in AB:
    c[x - 1].append(y - 1)
    c[y - 1].append(x - 1)
dep = [0] * N
from collections import deque

q = deque([(0, 0)])
v = [0] * N
v[0] = 1
A = [-1] * N
while q:
    p, d = q.popleft()
    dep[p] = d
    for n in c[p]:
        if v[n] == 0:
            v[n] = 1
            A[n] = p
            q.append((n, d + 1))
bit = N.bit_length()
d = [[0] * N for i in range(bit)]
d[0] = A
for i in range(bit - 1):
    for j in range(N):
        d[i + 1][j] = d[i][j] if d[i][j] == -1 else d[i][d[i][j]]


def db(N, K, s):
    for i in range(bit):
        if K & 1:
            s = d[i][s]
        K >>= 1
    return s


def lca(a, b):
    dd = dep[a] - dep[b]
    if dd > 0:
        a = db(N, dd, a)
    elif dd < 0:
        b = db(N, -dd, b)
    if a == b:
        return a
    for i in range(bit - 1, -1, -1):
        if d[i][a] != d[i][b]:
            a, b = d[i][a], d[i][b]
    return d[0][a]


for C, D in CD:
    x = dep[C - 1] + dep[D - 1] + dep[lca(C - 1, D - 1)] * 2
    print('Road' if x % 2 else 'Town')
