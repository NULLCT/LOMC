import sys

sys.setrecursionlimit(10000000)

n, q = map(int, input().split())
road = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    road[a].append(b)
    road[b].append(a)
qry = []
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    qry.append([c, d])

flag = [False] * n
zeroorone = [False] * n


def re(x, color):
    if not flag[x]:
        flag[x] = True
        ncolor = not color
        zeroorone[x] = ncolor
        for y in road[x]:
            re(y, ncolor)


re(0, True)

for i, j in qry:
    if zeroorone[i] == zeroorone[j]:
        print('Town')
    else:
        print('Road')
