#スタック、キューを使う
from collections import deque

N, Query = map(int, input().split())

G = []
for _ in range(N):
    G.append([])

#距離の配列
dist = []
for _ in range(N):
    dist.append(-1)

#BFSで使うキュー
Q = deque()

#入力からグラフを生成
for i in range(N - 1):
    #各頂点の情報を読み込み
    ms, me = map(int, input().split())
    #0オリジン
    ms -= 1
    me -= 1
    #無向グラフ
    G[ms].append(me)
    G[me].append(ms)


def bfs(s):
    #始点sをキューに追加
    Q.append(s)
    dist[s] = 0

    while len(Q) > 0:
        i = Q.popleft()  #キューの頂点をiに取り出す
        #uに未訪問の隣接ノードがある限りキューに入れる
        for j in G[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                Q.append(j)


# クエリを読み込むがその都度BFSしてたら間に合わない
# 予めある地点からの距離を求めておき各クエリにおいて、その距離の偶奇を調べることによって
# 道で出会うか、街で出会うか判定できる。
# 両方の偶奇が一緒 → 街で出会う。両方の偶奇が一致しない → 道で出会う。
# 偶奇が一緒かどうかの判定は足して偶数であれば 一致 合わなければ 不一致 である。

#距離の配列
dist = []
for _ in range(N):
    dist.append(-1)

#ある地点からの距離を計算しておく。
bfs(0)

for i in range(Query):
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    if (dist[s] + dist[t]) % 2 == 0:
        print('Town')
    else:
        print('Road')
