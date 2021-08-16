import math
from sys import setrecursionlimit

setrecursionlimit(1000000)


def ADJ(pos, ppos=None):
    log.append(pos)
    for i in D[pos - 1]:
        if i != ppos:
            d[i - 1] = d[pos - 1] + 1
            ADJ(i, pos)
    if d[pos - 1] > 0:
        D[pos - 1] = [
            log[-((2**j) + 1)]
            for j in range(int(math.log(d[pos - 1], 2)) + 1)
        ]
    else:
        D[pos - 1] = []
    log.pop()


def Search(a, b, n):
    #print(a, b, n)
    for k in range(len(D[b - 1])):
        if D[a - 1][k] == D[b - 1][k]:
            if k <= 1:
                return n + (2**(k + 1))
            else:
                return Search(D[a - 1][k - 1], D[b - 1][k - 1], n + (2**(k)))
    else:
        return Search(D[a - 1][-1], D[b - 1][-1], n + (2**(len(D[b - 1]))))


N, Q = map(int, input().split())
D = [[] for _ in range(N)]
d = [0] * N
for i in range(N - 1):
    x, y = map(int, input().split())
    D[x - 1].append(y)
    D[y - 1].append(x)
log = []
ADJ(N // 2)
#print(d)
#print(*D, sep = "\n")
for i in range(Q):
    a, b = map(int, input().split())
    sa = d[b - 1] - d[a - 1]
    if sa < 0:
        a, b = b, a
        sa *= -1
    print('Town' if sa % 2 == 0 else 'Road')
