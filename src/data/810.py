from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe


def LI():
    return list(map(int, input().split()))


def II():
    return int(input())


def chkprint(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print(', '.join(
        names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args))


N, Q = LI()
F = [[] for i in range(N + 1)]
#print("F",F)

for _ in range(N - 1):
    a, b = LI()
    F[a].append(b)
    F[b].append(a)
#print("F",F)
#print("a",a,"b",b)
# aから始める

DD = [0 for i in range(N + 1)]

root = a
A = [False for i in range(N + 1)]
A[a] = True
DQ = deque([[a, 0]])

while DQ:
    v, cost = DQ.pop()
    DD[v] = cost
    for nv in F[v]:
        if A[nv] == False:
            A[nv] = True
            DQ.append([nv, cost + 1])
#print("DD",DD)
for _ in range(Q):
    c, d = LI()
    if abs(DD[c] - DD[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
