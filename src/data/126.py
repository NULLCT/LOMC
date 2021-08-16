import queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# キューを使用
que = queue.Queue()
color = [-1] * N

# 先頭を0に固定
color[0] = 0
que.put(0)

# 各街を2色に塗る
while not que.empty():
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)

# 色が同じならばTown, そうでないならRoadを出力
for i in range(Q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print("Town")
    else:
        print("Road")
