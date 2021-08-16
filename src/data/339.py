i1 = lambda: input()
i2 = lambda: int(input())
i3 = lambda: map(int, input().split())
i4 = lambda n: [list(map(int, input().split()) for _ in range(n))]

import sys

sys.setrecursionlimit(1000000)

N, Q = i3()

INF = float('infinity')

G = [[] for _ in range(N + 1)]
for i in range(N - 1):
    s, t = i3()
    G[s].append(t)
    G[t].append(s)

# N=4
# Q=1
# G=[[], [2], [1,3,4], [2], [2]]
# S=[[1,2]]

V = [0] * (N + 1)


def dfs(i, count):
    if V[i] != 0: return
    V[i] = count
    for p in G[i]:
        dfs(p, count + 1)
    return


R = 1
dfs(R, 0)
S = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    c, d = S[i]
    if (V[c] + V[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
