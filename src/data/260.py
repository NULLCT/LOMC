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

anss = []
for c, d in cds:
    c, d = c - 1, d - 1
    depth1, depth2 = depths[c], depths[d]
    if depth1 % 2 != depth2 % 2:
        anss.append('Road')
    else:
        anss.append('Town')

print('\n'.join(anss))
