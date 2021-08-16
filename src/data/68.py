import sys

sys.setrecursionlimit(10**5)  # 上限設定

N, Q = map(int, input().split())
tmpA = [list(map(int, input().split())) for _ in range(N - 1)]
A = [a[0] for a in tmpA]
B = [a[1] for a in tmpA]
tmpB = [list(map(int, input().split())) for _ in range(Q)]
C = [b[0] for b in tmpB]
D = [b[1] for b in tmpB]
"""変数初期化"""
route = []
dep = []
"""リスト系初期化"""
for _ in range(N):
    route.append([])
    dep.append(0)
"""ルートの初期化"""
for i in range(N - 1):
    route[A[i] - 1].append(B[i] - 1)
    route[B[i] - 1].append(A[i] - 1)


def dfs(x, parent=-1):
    """深さ優先探索"""
    for i in route[x]:
        if (i == parent):
            continue
        dep[i] = dep[x] + 1
        dfs(i, x)


dfs(0)

for i in range(Q):
    if ((dep[C[i] - 1] + dep[D[i] - 1]) % 2 == 0):
        print("Town")
    else:
        print("Road")
