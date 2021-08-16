#import numpy as np
#from scipy.sparse.csgraph import shortest_path
from collections import deque

# BFS(幅優先探索)
N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
#print(G)  # 上三角行列になる

visited = [False] * N  # 頂点iが訪問済か否か(0-index)
d = deque()
d.append(0)  # 頂点1を探索済に
visited[0] = True

inf = 2 << 30
D = [inf] * N  # 頂点1からの距離を保存する配列
D[0] = 0  # 頂点1から頂点1までの距離は0

while d:  # dが空ではない間続ける
    # BFSなのでスタックを利用
    v = d.popleft()  # 先頭の要素を削除しそれをvに保存
    for i in G[v]:
        if visited[i] == False:  # 未訪問の頂点である場合
            visited[i] = True  # 訪問済にする
            D[i] = D[v] + 1  # 頂点v->iへ移動可能なので+1
            d.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    if D[c - 1] % 2 == D[d - 1] % 2:
        print('Town')
    else:
        print('Road')
''' この方法はTLE
L = np.array(l)
for i in range(Q):
  c, d = map(int, input().split())
  S = shortest_path(L)
  #print(S)
  if S[c - 1][d - 1] % 2:
    print('Road')
  else:
    print('Town')
'''

# 重みが全て1だからBFS, 重みがある時はダイクストラ
