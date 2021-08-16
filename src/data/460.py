import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
a = []
b = []
c = []
d = []
town = [[] for _ in range(N)]  # 隣接リスト

for i in range(N - 1):
    a_tmp, b_tmp = map(int, input().split())
    a.append(a_tmp)
    b.append(b_tmp)

for i in range(N - 1):
    town[a[i] - 1].append(b[i] - 1)
    town[b[i] - 1].append(a[i] - 1)

dep = [-1] * N


def dfs(v, _dep=0, p=-1):
    dep[v] = _dep
    for u in town[v]:
        if u != p:
            dfs(u, _dep + 1, v)


dfs(0)
col = [i % 2 for i in dep]

for _ in range(Q):
    c, d = map(int, input().split())
    if col[c - 1] == col[d - 1]:
        print('Town')
    else:
        print('Road')
