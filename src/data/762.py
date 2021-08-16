#幅優先探索(グラフ)
import queue

N, Q = map(int, input().split())
dist = [-1 for i in range(N)]  #距離
que = queue.Queue()
nodes = [[] for i in range(N)]

#nodeの入力
for i in range(N - 1):
    a, b = map(int, input().split())
    nodes[a - 1].append(b - 1)
    nodes[b - 1].append(a - 1)

# 始点の設定
que.put(0)
dist[0] = 0

#キューが無くなるまでループ
while not que.empty():
    cur = que.get()

    for next_node in nodes[cur]:
        if dist[next_node] != -1: continue
        que.put(next_node)
        dist[next_node] = dist[cur] + 1

for i in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] + dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
