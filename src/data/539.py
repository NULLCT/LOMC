def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


# おまじない
import sys
import pdb

sys.setrecursionlimit(1000000)
# 入力の読み込み
N, Q = map(int, input().split())
G = [[] for i in range(N)]
# G[i] は王国iから道路で直接繋がっている王国のリスト
for i in range(N - 1):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

visited_time = [-1] * (N)  # 訪れる時間を記録
temp = [False] * (N)  # 訪れたかを記録


# dfs
def dfs(v, dist):
    if temp[v]: return  # 同じ頂点を2度以上調べないためのreturn
    temp[v] = True
    visited_time[v] = dist
    for vv in G[v]:
        dfs(vv, dist + 1)


ans = 0
# (スタート王国，訪れた時刻)
dfs(0, 0)

# 二部グラフ判定
for _ in range(Q):
    c, d = li_int_sp()
    if abs(visited_time[c - 1] - visited_time[d - 1]
           ) % 2 == 1:  #(奇数 and 奇数) or (偶数 and 偶数)なら街で出会う．それ以外なら道路で出会う．
        print('Road')
    else:
        print('Town')
