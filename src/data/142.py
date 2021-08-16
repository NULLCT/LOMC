'''
[問題]
https://atcoder.jp/contests/abc209/tasks/abc209_d

[解法]
https://youtu.be/FEDp2Kzc7jk?t=3245
　二分木の問題。
　c,d間の距離の偶奇が答えになる。
　最小共通祖先（Lowest Common Ancestor）を求めなければならない気がするが、偶奇の判定はc,dの深さだけで問題ない。
　depを深さと考えて、最短距離は
　dep[c] + dep[d] - dep[lca] * 2
　lcaはx2なので、lcaが奇数でも偶数でも結果偶数になる。よってlcaは偶奇に影響しない。

[参考]
二分木における最小共通祖先（Lowest Common Ancestor）の探索
https://qiita.com/maebaru/items/0fec7d2987c4a1efaa8a

https://atcoder.jp/contests/abc209/submissions/24350316
'''

import sys

sys.setrecursionlimit(10**6)  # 再帰上限の引き上げ
input = sys.stdin.readline

INF = 10**18 + 7

N, Q = map(int, input().split())

route = [[] for _ in range(N)]
dep = [0] * N

for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    route[A].append(B)
    route[B].append(A)


# Depth First Searchで深さを計算する
def dfs(x, last=-1):
    for to in route[x]:
        if to == last:
            continue
        dep[to] = dep[x] + 1
        dfs(to, x)


dfs(0)

# クエリ処理
for _ in range(Q):
    C, D = map(int, input().split())

    if (dep[C - 1] + dep[D - 1]) % 2 == 1:
        # 経路が奇数なら道
        print("Road")
    else:
        print("Town")
