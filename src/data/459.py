def resolve():
    from collections import deque
    import numpy as np

    N, Q = map(int, input().split())

    # 各町を頂点として、リストで接続先の頂点を表現するグラフ
    G = [[] for i in range(N + 1)]

    # 各頂点の色
    # 0, 1: 色付き -1:色なし
    distance = [np.inf for i in range(N + 1)]

    # 町番号をインデックスとした接続先の町をリストで格納するテーブルを作成
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # bfsで全経路を探索し、2部グラフの各頂点に色をつける
    def bfs():
        start = 1
        q = deque()
        q.append(start)
        distance[start] = 0

        while q:
            x = q.popleft()
            for i in G[x]:
                if distance[i] == np.inf:
                    distance[i] = distance[x] + 1
                    q.append(i)

    bfs()

    # クエリを処理する
    for i in range(Q):
        c, d = map(int, input().split())

        if abs(distance[c] - distance[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


resolve()
