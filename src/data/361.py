MOD = 10**9 + 7
INF = float('inf')
AZ = "abcdefghijklmnopqrstuvwxyz"

#############
# Functions #
#############


######INPUT######
def I(t):
    return t(input().strip())


def IM(t):
    return map(t, input().split())


def IL(t):
    return list(map(t, input().split()))


def ILs(t, n):
    return list(t(input()) for _ in range(n))


def ILL(t, n):
    return [list(map(t, input().split())) for _ in range(n)]


n, q = IM(int)
e = [INF for _ in range(n)]
e[0] = 0
edge = [[] for i in range(n)]

for i in range(n - 1):
    a, b = IM(int)
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

s = [0]
while s:
    t = s.pop(0)
    for i in edge[t]:
        if e[i] == INF:
            e[i] = e[t] + 1
            s.append(i)

for i in range(q):
    c, d = IM(int)
    if (e[c - 1] % 2) == (e[d - 1] % 2):
        print('Town')
    else:
        print('Road')
