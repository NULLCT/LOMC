import sys

sys.setrecursionlimit(10**6)


def dfs(v, pre, d):
    for nv in G[v]:
        if nv == pre: continue
        depth[nv] = d + 1
        dfs(nv, v, d + 1)


N, Q = map(int, input().split())
G = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

depth = [-1] * (N)  # 根（root）からの距離
depth[0] = 0  # rootの初期値を0とする。
# グラフに根からの距離と2**k上の点を記録。
dfs(0, -1, 0)

for q in range(Q):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    ans = 0
    if abs(depth[ci] - depth[di]) % 2 == 0:
        print('Town')
    else:
        print('Road')
