import sys

sys.setrecursionlimit(100000)
n, q = map(int, input().split())
r = list([] for i in range(n - 1))
for i in range(n - 1):
    r[i] = list(map(int, input().split()))
t = list([] for i in range(n))
for i in range(n - 1):
    t[r[i][0] - 1].append(r[i][1] - 1)
    t[r[i][1] - 1].append(r[i][0] - 1)
l = [0] * n


def dt(x, y, z):
    for i in t[x]:
        if i != z:
            l[i] = y + 1
            dt(i, y + 1, x)


dt(0, 0, None)
for i in range(q):
    c, d = map(int, input().split())
    f = l[c - 1] + l[d - 1]
    if f % 2 == 0:
        print('Town')
    else:
        print('Road')
