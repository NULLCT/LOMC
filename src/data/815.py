import math
from collections import deque, Counter
from itertools import product, combinations, permutations

lkopmn, axsder = map(int, input().split())
hyujg = [list(map(int, input().split())) for _ in range(lkopmn - 1)]
anmjki = [list(map(int, input().split())) for _ in range(axsder)]
QWS = [[] for _ in range(lkopmn)]
for ptgfre in range(lkopmn - 1):
    dfre, juinb = hyujg[ptgfre][0], hyujg[ptgfre][1]
    dfre -= 1
    juinb -= 1
    QWS[dfre].append(juinb)
    QWS[juinb].append(dfre)

akjm = [-1] * lkopmn
poewq = deque()
vbnjui = 0
akjm[vbnjui] = 0
poewq.append(vbnjui)
while (poewq):
    zxcfrt = poewq.popleft()
    for satyuj in QWS[zxcfrt]:
        if akjm[satyuj] != -1:
            continue
        else:
            akjm[satyuj] = akjm[zxcfrt] + 1
            poewq.append(satyuj)
for bnjcd in anmjki:
    if (akjm[bnjcd[1] - 1] - akjm[bnjcd[0] - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
