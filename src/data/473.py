from collections import deque

N, Q = map(int, input().split())

# 各町を頂点として、リストで接続先の頂点を表現するグラフ
table = [[] for i in range(N + 10)]
# 各頂点の色
# 0, 1: 色付き -1:色なし
colors = [-1 for i in range(N + 10)]

# 町番号をインデックスとした接続先の町をリストで格納するテーブルを作成
for i in range(N - 1):
    a, b = map(int, input().split())
    table[a - 1].append(b - 1)
    table[b - 1].append(a - 1)


# bfsで全経路を探索し、2部グラフの各頂点に色をつける
def bfs():
    start = 0
    q = deque()
    q.append(start)
    colors[start] = 1

    while q:
        x = q.popleft()
        for i in table[x]:
            if colors[i] == -1:
                colors[i] = 1 - colors[x]
                q.append(i)


bfs()
#print("colors={}".format(colors))

# クエリを処理する
for i in range(Q):
    c, d = map(int, input().split())
    #print("i={} c={} d={}".format(i,c,d))
    if colors[c - 1] == colors[d - 1]:
        print("Town")
    else:
        print("Road")
