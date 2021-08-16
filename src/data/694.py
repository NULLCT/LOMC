import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
g = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

cnt = [0] * N


def f(cur, par, i):
    cnt[cur] = i
    for chi in g[cur]:
        if chi != par:
            f(chi, cur, i + 1)


f(0, -1, 0)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    tmp = (cnt[d] - cnt[c]) % 2
    if tmp:
        print('Road')
    else:
        print('Town')
