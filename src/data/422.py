import sys


def input():
    return sys.stdin.readline().rstrip()


from collections import deque

n, q = map(int, input().split())  # 頂点数と辺数

# グラフ入力受け取り (ここでは無向グラフを想定)
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * n  # 全頂点を -1 (未訪問) に初期化
pos = deque()  # キュー

# 初期条件 (頂点 0 を始点とする)
dist[0] = 0
pos.append(0)

# 幅優先探索 (キューが空になるまで探索を行う)
while len(pos) > 0:
    v = pos.popleft()  # キューから先頭の頂点を取り出す
    for nv in graph[v]:
        # 既に訪問済みの頂点は探索しない
        if dist[nv] != -1:
            continue
        # 新たな頂点 nv について距離情報を更新してキューに追加する
        dist[nv] = dist[v] + 1
        pos.append(nv)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
