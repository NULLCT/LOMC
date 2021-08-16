from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())
adjL = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    adjL[a].append(b)
    adjL[b].append(a)
cds = [tuple(map(int, input().split())) for _ in range(Q)]


def bfsTree(vRoot):
    depths[vRoot] = 0
    QQQ = deque([vRoot])
    while QQQ:
        vNow = QQQ.popleft()
        vPar = pars[vNow]
        depth2 = depths[vNow] + 1
        for v2 in adjL[vNow]:
            if v2 == vPar: continue
            pars[v2] = vNow
            depths[v2] = depth2
            QQQ.append(v2)


numV = N  ###
vRoot = 0  ###

pars = [-1] * (numV)
depths = [-1] * (numV)

bfsTree(vRoot)


def getParssLCA(pars):
    numV = len(pars)
    maxD = numV.bit_length() - 1
    parss = [[-1] * (numV) for _ in range(maxD + 1)]
    for v in range(numV):
        parss[0][v] = pars[v]
    for d in range(1, maxD + 1):
        for v in range(numV):
            if parss[d - 1][v] != -1:
                parss[d][v] = parss[d - 1][parss[d - 1][v]]
    return parss, maxD


parss, maxD = getParssLCA(pars)


def getLCA(x, y):
    if depths[x] < depths[y]:
        x, y = y, x
    diff = depths[x] - depths[y]
    for d in range(maxD + 1):
        if (diff >> d) & 1:
            x = parss[d][x]
    if x == y:
        return x
    for d in reversed(range(maxD + 1)):
        if parss[d][x] != parss[d][y]:
            x = parss[d][x]
            y = parss[d][y]
    return parss[0][x]


anss = []
for c, d in cds:
    c, d = c - 1, d - 1
    LCA = getLCA(c, d)
    dist = abs(depths[c] - depths[LCA]) + abs(depths[d] - depths[LCA])
    if dist % 2:
        anss.append('Road')
    else:
        anss.append('Town')

print('\n'.join(anss))
