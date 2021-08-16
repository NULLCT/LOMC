n, q = map(int, input().split())

from heapq import heappush, heappop


class dijkstra:
    # 初期化(ノード数)
    def __init__(self, n):
        # ノード数
        self.num = n
        # エッジ情報の格納先　edge[start]=[(end,cost),(end,cost),・・・]
        self.edge = [[] for _ in range(n)]

    # エッジの追加(0index)
    def edge_add(self, start, end, cost):
        self.edge[start].append((end, cost))

    # スタート地点からそれぞれの点への最短距離を計算
    # O((ノード数+エッジ数)log(ノード数)
    def to_end(self, start):
        # 到達不能距離
        inf = 10**15
        # スタートからの距離
        dist = [inf] * self.num
        # 固定されているかどうか
        fixed = [False] * self.num
        # スタート地点からスタート地点への距離は0
        dist[start] = 0
        # スタート地点をキューに入れる
        hq = [(0, start)]
        while hq:
            # now_cost=今いる場所に書いてるコスト、now_place=今いる場所
            now_cost, now_place = heappop(hq)
            # すでに終わっていれば
            if fixed[now_place] == True:
                continue
            # 今いる場所のコストを固定
            fixed[now_place] = True
            # 今いる場所から行ける場所を順に回る
            for to_place, to_cost in self.edge[now_place]:
                # 固定されていなくて、よりコストが低いなら
                if fixed[to_place] == False and now_cost + to_cost < dist[
                        to_place]:
                    # コストを書き換え
                    dist[to_place] = now_cost + to_cost
                    # キューに入れる
                    heappush(hq, (dist[to_place], to_place))
        return dist


dij = dijkstra(n)
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    dij.edge_add(a, b, 1)
    dij.edge_add(b, a, 1)

dist = dij.to_end(0)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] % 2 == dist[d] % 2:
        print("Town")
    else:
        print("Road")
