### ----------------
### ここから
### ----------------

import sys
import itertools
import heapq
from collections import deque
from collections import Counter


def resolve():
    readline = sys.stdin.readline
    #INF = float('inf')
    #NAN = float('nan')
    #N=int(readline())
    N, Q = map(int, readline().rstrip().split())
    Adj = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, readline().rstrip().split())
        a -= 1
        b -= 1
        Adj[a].append(b)
        Adj[b].append(a)

    q = deque()
    q.appendleft(0)
    DONE = [False] * N
    DONE[0] = True
    D = [float("inf")] * N
    D[0] = 0
    while q:
        p = q.pop()
        for p2 in Adj[p]:
            if DONE[p2]:
                continue
            if (D[p] + 1) < D[p2]:
                D[p2] = D[p] + 1
                DONE[p2] = True
                q.appendleft(p2)

    for i in range(Q):
        c, d = map(int, readline().rstrip().split())
        c -= 1
        d -= 1
        if D[c] % 2 == D[d] % 2:
            print("Town")
        else:
            print("Road")

    #Arr=list(map(int, readline().rstrip().split()))
    #Arr=[list(map(int, readline().rstrip().split())) for _ in range(n)]
    #S=readline().rstrip()
    #print("Yes")
    #print("No")
    #q = deque()
    #c = Counter()

    return


if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで
### ----------------
