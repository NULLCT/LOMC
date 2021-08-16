#典型90 003
#木の直径は、任意の頂点sを選び、sからDFS/BFSを行い、最も遠い頂点uを探索する
#uからDFS/BFSを行い、最も遠い頂点vを探索する。uvの距離が答え

N, Q = map(int, input().split())

#隣接リストを使用
#FalseのN*0の二次元配列
graph = []
for i in range(0, N):

    #長さ0の一次元配列
    row = []
    graph.append(row)

#N-1本の辺を受け取る
for i in range(1, N):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    #uとvの間には辺がある
    graph[u].append(v)
    graph[v].append(u)

#根から各頂点に向かう。
#dequeを使えるようにする
from collections import deque


def bfs():
    #スタートからの最小移動回数dを管理する配列。値が負であれば未訪問
    d = [-1] * N

    #キューを用意し、スタートを入れる
    que = deque()
    que.append(s)
    d[s] = 0

    while que:
        #キューから取り出しながら探索
        p = que.popleft()
        #キューから取り出されたものの隣に行く。
        for i in graph[p]:
            if d[i] == -1:
                que.append(i)
                d[i] = d[p] + 1
    return d


s = 0
dist = bfs()

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] % 2 == dist[d] % 2:
        print("Town")
    else:
        print("Road")
