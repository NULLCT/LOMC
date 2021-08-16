# モジュールのインポート
import sys

sys.setrecursionlimit(1000000)

# 標準入力を取得
N, Q = list(map(int, input().split()))
g = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
q = []
for _ in range(Q):
    c, d = list(map(int, input().split()))
    q.append((c, d))

# 求解処理
t = {i: -1 for i in range(1, N + 1)}


def dfs(g: dict, t: dict, depth: int, node: int) -> None:
    if t[node] != -1:
        return
    t[node] = depth
    for child in g[node]:
        dfs(g, t, depth + 1, child)


dfs(g, t, 0, 1)

for c, d in q:
    if abs(t[c] - t[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
