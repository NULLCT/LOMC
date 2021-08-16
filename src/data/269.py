import sys

sys.setrecursionlimit(100000)
N, Q = map(int, input().split())
G = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def tansaku(p):
    for j in G[p]:
        if H[j] == 0:
            H[j] = H[p] + 1
            tansaku(j)


H = [0] * N
tansaku(0)
for l in range(Q):
    c, d = list(map(int, input().split()))
    if abs(H[c - 1] - H[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
