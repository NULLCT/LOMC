#D
from collections import deque


def bfs(x):
    e[x] = 0
    v = deque([x])

    while v:
        y = v.pop()
        for z in L[y]:
            if e[z] == -1:
                e[z] = e[y] + 1
                v.append(z)


###############################################

N, Q = map(int, input().split())
a = [0] * (N - 1)
b = [0] * (N - 1)
L = [[] for _ in range(N)]

for i in range(N - 1):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
    L[a[i]].append(b[i])
    L[b[i]].append(a[i])

e = [-1] * N  #距離・訪問
bfs(0)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    dist = abs(e[c] - e[d])
    if dist % 2 == 0:
        ans = "Town"
    else:
        ans = "Road"
    print(ans)
