import sys

input = sys.stdin.readline
n, q = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n - 1)]
l2 = [list(map(int, input().split())) for i in range(q)]

connection = [[] for i in range(n)]
for i in range(n - 1):
    connection[l[i][0] - 1].append(l[i][1] - 1)
    connection[l[i][1] - 1].append(l[i][0] - 1)


def bfs(v):
    distance = [-1] * n
    distance[v] = 0
    next = connection[v]
    next2 = set()
    visited = [-1] * n
    visited[v] = 1
    visitct = 1
    ct = 0
    while len(next) != 0 and visitct != n:
        ct += 1
        for i in range(len(next)):
            if visited[next[i]] == -1:
                distance[next[i]] = ct
                visited[next[i]] = 1
                visitct += 1
                for j in range(len(connection[next[i]])):
                    if visited[connection[next[i]][j]] == -1:
                        next2.add(connection[next[i]][j])
        next = list(next2)
        next2 = set()
    return distance


B = bfs(0)

par = [-1] * n
chi = [[] for i in range(n)]
root = 0

for i in range(n - 1):
    if B[l[i][0] - 1] < B[l[i][1] - 1]:
        par[l[i][1] - 1] = l[i][0] - 1
        chi[l[i][0] - 1].append(l[i][1] - 1)
    else:
        par[l[i][0] - 1] = l[i][1] - 1
        chi[l[i][1] - 1].append(l[i][0] - 1)


def eulerTour(par, chi):
    tank = [root]
    eulerTour = []
    left = [0] * n
    right = [-1] * n
    depth = [-1] * n
    eulerNum = -1
    de = -1

    while tank:
        q = tank.pop()
        if q >= 0:
            eulerNum += 1
            eulerTour.append(q)
            left[q] = eulerNum
            right[q] = eulerNum
            tank.append(~q)
            de += 1
            depth[q] = de
            for ch in chi[q]:
                tank.append(ch)
        else:
            de -= 1
            if ~q != root:
                eulerTour.append(par[~q])
                eulerNum += 1
                right[par[~q]] = eulerNum

    return eulerTour, depth, left, right


S = eulerTour(par, chi)[0]
depth = eulerTour(par, chi)[1]
F = eulerTour(par, chi)[2]

INF = (n, None)

M = 2 * n
M0 = 2**(M - 1).bit_length()
data = [INF] * (2 * M0)
for i, v in enumerate(S):
    data[M0 - 1 + i] = (depth[v], i)
for i in range(M0 - 2, -1, -1):
    data[i] = min(data[2 * i + 1], data[2 * i + 2])


def _query(a, b):
    yield INF
    a += M0
    b += M0
    while a < b:
        if b & 1:
            b -= 1
            yield data[b - 1]
        if a & 1:
            yield data[a - 1]
            a += 1
        a >>= 1
        b >>= 1


def LCA(u, v):
    fu = F[u]
    fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv + 1))[1]]


for i in range(q):
    x = depth[l2[i][0] - 1] + depth[l2[i][1] - 1] - 2 * depth[LCA(
        l2[i][0] - 1, l2[i][1] - 1)]
    if x % 2 == 1:
        print('Road')
    else:
        print('Town')
