from collections import deque

INF = 1 << 60
MOD = 10**9 + 7

N, Q = map(int, input().split())

# 無向グラフ
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
q = deque([])
parent = -1
dep = 1
q.append((0, dep, parent))

while len(q) > 0:
    v, dep, parent = q.popleft()
    for vv in to[v]:
        if vv == parent: continue
        dep_list[vv] = dep
        q.append((vv, dep + 1, v))

# それぞれのクエリにおいて c と d の経路の偶奇を求める
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    parity = dep_list[c] + dep_list[d]
    print("Town" if parity % 2 == 0 else "Road")
