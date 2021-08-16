import sys
from collections import deque


def source():
    spi = lambda x: map(int, x.split())
    S = sys.stdin.read().splitlines()

    n, q = spi(S[0])
    roads = [list(spi(row)) for row in S[1:n]]

    G = [[] for _ in range(n)]
    for s, e in roads:
        s -= 1
        e -= 1
        G[s] += [e]
        G[e] += [s]

    q_list = [list(spi(row)) for row in S[n:n + q]]
    queries = [[i - 1, v - 1] for i, v in q_list]

    return n, q, G, queries


def bfs(n, G):
    # キュー
    queue = deque([0])
    # 最短経路の記録
    dp = [-1] * n
    # スタート地点は0に
    dp[0] = 0

    while queue:
        # 取り出し
        target = queue.pop()
        # targetから行ける場所
        children = G[target]
        for child in children:
            if dp[child] == -1:
                dp[child] = dp[target] + 1
                queue.append(child)

    # dpを返す
    return dp


def solve(n, q, G, queries):
    # bfsを実行
    # BFSを毎回やっていると時間がかかってTLEになるので、差分で求める
    dp = bfs(n, G)

    for c, d in queries:
        dpc, dpd = dp[c], dp[d]
        if dpc % 2 == dpd % 2:
            print('Town')
        else:
            print('Road')


def main():
    n, q, G, queries = source()
    solve(n, q, G, queries)


if __name__ == '__main__':
    main()
