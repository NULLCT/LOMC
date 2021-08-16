import sys
import math

sys.setrecursionlimit(10**5)

N, Q = map(int, input().split())
tmpA = [list(map(int, input().split())) for _ in range(N - 1)]
A = [a[0] for a in tmpA]
B = [a[1] for a in tmpA]
tmpB = [list(map(int, input().split())) for _ in range(Q)]
C = [b[0] for b in tmpB]
D = [b[1] for b in tmpB]

# N = 4
# Q = 1
# A = [1, 2, 2]
# B = [2, 3, 4]
# C = [1]
# D = [2]
"""変数初期化"""
route = []
dep = []
"""
A.append[-1]  # 最後の値の判別
B.append[-1]  # 最後の値の判別
"""
"""リスト系初期化"""
for _ in range(N):
    route.append([])
    dep.append(0)
"""ルートの初期化"""
for i in range(N - 1):
    route[A[i] - 1].append(B[i] - 1)
    route[B[i] - 1].append(A[i] - 1)


def dfs(x, last=-1):
    """深さ優先探索"""
    for i in route[x]:
        if (i == last):
            continue
        dep[i] = dep[x] + 1
        dfs(i, x)


dfs(0)

for i in range(Q):
    if ((dep[C[i] - 1] + dep[D[i] - 1]) % 2 == 0):
        print("Town")
    else:
        print("Road")
