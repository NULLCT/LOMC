class Dijkstra():
    class Edge():
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        self.G = [[] for i in range(V)]  # 隣接リストG[u][i] := 頂点uのi個目の隣接辺
        self._E = 0  # 辺の数
        self._V = V  # 頂点の数

    def E(self):
        return self._E

    def V(self):
        return self._V

    def add(self, _from, _to):
        self.G[_from].append(self.Edge(_to, 1))
        self._E += 1

    def shortest_path(self, s):
        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        d = [float("INF")] * self._V
        d[s] = 0
        heapq.heappush(que, (0, s))  # 始点の(最短距離, 頂点番号)をヒープに追加する
        while len(que) != 0:
            cost, v = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # dの更新
                    heapq.heappush(
                        que,
                        (d[e.to], e.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d


N, Q = map(int, input().split())
djk = Dijkstra(N)
for i in range(N - 1):
    u, v = map(int, input().split())
    djk.add(u - 1, v - 1)
    djk.add(v - 1, u - 1)
d1 = djk.shortest_path(0)
for i in range(Q):
    c, d = map(int, input().split())
    if (d1[c - 1] + d1[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
