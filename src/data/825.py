# ダイクストラ法

# 使い方
# ① collectionをインポート
# ② n,mの取得
# ③ nodeのリストnodesの大枠を作成
# ④ 隣接ノード、道の所要時間など、道の情報をnodeに追加
# ⑤ 開始位置を設定
# ⑥ 最短距離探索コードの修正
from collections import deque  # ①
import sys

sys.setrecursionlimit(10**6)
INF = 10**18

# # n:nodeの数,　m:道の数
# # たいてい下のコードで取得可能

n, q = map(int, input().split())  # ②


class Node:
    def __init__(self, number):
        self.number = number  # 名前をつける
        self.depth = INF
        # node,所要時間のリストを格納
        # node: このノードから進むことのできるnode
        # 所要時間:　進むのにかかる時間
        self.road_information = []


# #nodeのリストを作る。たいてい下のコードで元をつくり、次のコードで中身を入れる。
nodes = [None] + [Node(i) for i in range(1, n + 1)]  # ③
nodes[1].depth = 0
# # nodeの道の情報を入れる。④
for i in range(n - 1):
    a, b = map(int, input().split())
    nodes[a].road_information.append([nodes[b], 1])
    nodes[b].road_information.append([nodes[a], 1])

que = deque()

que.append(nodes[1])

# 最短距離計算コード
while que:
    node = que.popleft()
    for child, cost in node.road_information:
        if child.depth == INF:
            child.depth = node.depth + 1
            que.append(child)
        # N: 頂点数
        # G[v]: 頂点vの子頂点 (親頂点は含まない)
min_time = [INF] * (n + 1)

for i in range(1, n + 1):
    min_time[i] = nodes[i].depth
    # Euler Tour の構築

# nodes = nodes[1:]
# S = []
# F = [0] * n
# depth = [0]*n

# def dfs(parent, v, d):
#     F[v.number-1] = len(S)
#     depth[v.number-1] = d
#     S.append(v.number-1)
#     for w, cost in nodes[v.number-1].road_information:
#         if parent != w or parent is None:
#             dfs(v, w, d+1)
#             S.append(v.number-1)

# dfs(None, nodes[0], 0)

# # 存在しない範囲は深さが他よりも大きくなるようにする
# INF = (n, None)

# # LCAを計算するクエリの前計算
# M = 2*n
# M0 = 2**(M-1).bit_length()
# data = [INF]*(2*M0)
# for i, v in enumerate(S):
#     data[M0-1+i] = (depth[v], i)
# for i in range(M0-2, -1, -1):
#     data[i] = min(data[2*i+1], data[2*i+2])

# # LCAの計算 (generatorで最小値を求める)

# def _query(a, b):
#     yield INF
#     a += M0
#     b += M0
#     while a < b:
#         if b & 1:
#             b -= 1
#             yield data[b-1]
#         if a & 1:
#             yield data[a-1]
#             a += 1
#         a >>= 1
#         b >>= 1

# # LCAの計算 (外から呼び出す関数)

# def query(u, v):
#     fu = F[u]
#     fv = F[v]
#     if fu > fv:
#         fu, fv = fv, fu
#     return S[min(_query(fu, fv+1))[1]]

for i in range(q):
    c, d = map(int, input().split())
    ans = min_time[c] + min_time[d]
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
