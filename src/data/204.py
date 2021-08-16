# coding : utf-8


def main():
    N, num_Q = map(int, input().split())

    # グラフの初期化
    city = {}
    for i in range(1, N + 1):
        city[str(i)] = []

    # グラフの作成
    for i in range(N - 1):
        a, b = map(int, input().split())
        city[str(a)].append(b)
        city[str(b)].append(a)

    # 1の街を根ノードとして、深さを記録していく
    city_depth = {}
    Q = [1]  # Qに根ノードだけ加えておき、子ノードをどんどん加えていく。
    depth = 0
    while (len(Q) >= 1):  # Qが空になるまで繰り返す。
        new_Q = []
        for q in Q:
            # Qに入っているノードの深さを記録
            city_depth[str(q)] = depth
            # Qに入っているノードの子ノードをQに加える。ただし深さが既知は除く。
            for q_child in city[str(q)]:
                if not str(q_child) in city_depth:
                    new_Q.append(q_child)
                else:
                    pass
            # qをQから取り除く
        Q = new_Q
        depth += 1

    # 次にクエリに答えていく
    for i in range(num_Q):
        c, d = map(int, input().split())
        if abs(city_depth[str(c)] - city_depth[str(d)]) % 2 == 0:
            print("Town")
        else:
            print("Road")


main()
