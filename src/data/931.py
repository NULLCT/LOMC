def resolve():
    from collections import deque
    # クエリ先読みっぽいな
    # 木構造なので最短経路しか無いはず。
    # 距離が偶数なら Town、そうで無いなら Road
    # アルゴリズム名がわからん
    # ダブリング
    N, Q = map(int, input().split(" "))
    EDGE = [set() for _ in range(N)]
    for _ in range(N - 1):
        a, b = [int(x) - 1 for x in input().split(" ")]
        EDGE[a].add(b)
        EDGE[b].add(a)

    k = N.bit_length()
    # データの構築
    D = [[0] * N for _ in range(k)]
    D[0][0] = -1
    nexts = deque()
    nexts.append(0)
    checked = [False] * N
    checked[0] = True
    while nexts:
        current = nexts.popleft()
        for n in EDGE[current]:
            if checked[n]: continue
            checked[n] = True
            D[0][n] = D[0][current] + 1
            nexts.append(n)

    # for i in range(k-1):
    #   for j in range(N):
    #     D[i+1][j]=D[i][D[i][j]]

    for i in range(Q):
        a, b = [int(x) - 1 for x in input().split(" ")]
        # a の深さを求める
        d_a = D[0][a]
        d_b = D[0][b]
        if abs(d_a - d_b) % 2:
            print("Road")
        else:
            print("Town")
        # d_a = 0
        # c = a
        # while c != 0:
        #   D[]


import sys
if sys.argv[-1] == './Main.py':
    resolve()
