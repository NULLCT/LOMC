import queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
#グラフに入れてる
que = queue.Queue()
color = [-1] * N
color[0] = 0
que.put(0)
#1を頂点に幅全
while not que.empty():
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            #-1なら未探索
            color[i] = 1 - color[t]
            #これで0か，1かに別れる
            que.put(i)
for i in range(Q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print("Town")
    else:
        print("Road")
