# クエリでない入力部分の前処理
N, Q = list(map(int, input().split()))
# 隣接リスト(A)を作成
A = [[] * 1 for _ in range(N)]
for i in range(N - 1):
    a, b = list(map(int, input().split()))
    A[a - 1].append(b - 1)
    A[b - 1].append(a - 1)
# 基準点からの通過辺数の偶奇で各点を分類
P = [None] * N  # 各点の基準点からの通過辺数の偶奇のリスト
e = 0  # 基準点からの通過辺数の偶奇
F = [0]  # 考察対象の点のリスト(初期値は基準点)
for i in range(N):
    F_n = []  # 次回ループでのF
    for p in F:
        P[p] = e
        F_n.extend(A[p])
    F = [j for j in F_n if P[j] == None]
    e = 1 - e

# クエリの処理
for i in range(Q):
    c, d = list(map(int, input().split()))
    if P[c - 1] == P[d - 1]:
        print("Town")
    else:
        print("Road")
