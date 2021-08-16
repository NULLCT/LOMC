def chk(i, f):
    f = (f + 1) % 2
    ablist[i] = f
    for r in route[i]:
        if ablist[r] == INF:
            chk(r, f)
    return


import sys

sys.setrecursionlimit(100000)

n, q = map(int, input().split())

INF = float('INF')
ablist = [INF] * n
route = []
for i in range(n):
    route.append([])

for i in range(n - 1):
    a, b = map(int, input().split())
    route[a - 1].append(b - 1)
    route[b - 1].append(a - 1)

#print(route)
chk(0, 0)
#print(ablist)

for i in range(q):
    c, d = map(int, input().split())
    if (ablist[c - 1] + ablist[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
