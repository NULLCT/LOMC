import sys

sys.setrecursionlimit(10**9)


def dfs(v: int, _dep=0, parent=-1):
    dep_list[v] = _dep
    for vv in to[v]:
        # 親に戻るルートの場合はスキップ（無限再帰を防ぐ）
        if vv == parent: continue
        dfs(vv, _dep + 1, v)


N, Q = map(int, input().split())

# 隣接リスト
to = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

# 全頂点の深さを格納する配列
dep_list = [0] * N

# 全頂点の深さを深さ優先探索で求める
dfs(0)

# それぞれのクエリにおいて c と d の経路の偶奇を求める
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    parity = dep_list[c] + dep_list[d]
    print("Town" if parity % 2 == 0 else "Road")
