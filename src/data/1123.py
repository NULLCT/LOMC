import sys

sys.setrecursionlimit(10**8)

N, Q = map(int, input().split())
L = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)
P = [0] * (N + 1)
T = [0] * (N + 1)


def dfs(p, cnt):
    P[p] = cnt
    T[p] = 1
    for l in L[p]:
        if T[l] == 0:
            dfs(l, cnt + 1)


dfs(1, 0)

for i in range(Q):
    a, b = map(int, input().split())
    if (P[a] + P[b]) % 2 == 0:
        print('Town')
    else:
        print('Road')
