# ------------- ココカラ提出 -------------
import sys

n, q = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)


def BFS(G, s):
    from collections import deque
    N = len(G)  # グラフのサイズ

    # 探索のためのデータ構造
    dist = [-1 for _ in range(N)]  # 全ての頂点を未訪問に
    que = deque()  # 空のスタック

    # 初期条件
    que.append(s)  # キューにenqueue
    dist[s] = 0

    # todoがからになるまで探索を行う
    while (que):
        v = que.popleft()  # キューからデキュー

        # vからたどれる頂点をすべて調べる
        for x in G[v]:
            # 既に探索済みの頂点は探索しない
            if dist[x] != -1:
                continue

            # 探索済みにセットして、todoに挿入
            dist[x] = dist[v] + 1
            que.append(x)

    return dist


dist = BFS(g, 0)

for i in range(q):
    c, d = map(int, sys.stdin.readline().split())
    c = c - 1
    d = d - 1

    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")

# ------------- ココマデ提出 -------------
