#N 個の街と N−1 本の道路なのでループはない。木構造
#根への距離をそれぞれ求めて、和が2で割り切れるかで判断できそう

from collections import defaultdict
from collections import deque

N, Q = map(int, input().split())

connect_nodes = defaultdict(set)

for i in range(N - 1):
    a, b = map(int, input().split())
    connect_nodes[a].add(b)
    connect_nodes[b].add(a)

dist = [-1 for _ in range(N + 1)]  #1からの距離。到達不可なら-1
is_visited = [False for _ in range(N + 1)]  #訪問フラグ

#function 幅優先探索(v)
search_deque = deque()  #Q ← 空のキュー
is_visited[1] = True  #v に訪問済みの印を付ける
search_deque.append(1)  #v を Q に追加
dist[1] = 0

while len(search_deque) != 0:  #while Q が空ではない do
    node = search_deque.popleft()  #    v ← Q から取り出す
    #    v を処理する
    for connect_node in connect_nodes[node]:  #    for each v に接続している頂点 i do
        if is_visited[connect_node] == False:  #        if i が未訪問 then
            is_visited[connect_node] = True  #            iに訪問済みの印を付ける
            search_deque.append(connect_node)  #            i を Q に追加
            dist[connect_node] = dist[
                node] + 1  #(左記は距離が全点間1固定の時。異なる場合は読み込み部分と共に変更すること)

for i in range(Q):
    c, d = map(int, input().split())

    if (dist[c] + dist[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
