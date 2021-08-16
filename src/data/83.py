import queue

N, Q = map(int, input().split())

G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()
que.put(0)
color = [-1] * N
color[0] = 0
while not que.empty():
    # t = 親になるノード
    t = que.get()
    for i in G[t]:
        # color[i] == -1ならノードIは未探索
        if color[i] == -1:
            color[i] = 1 - color[t]
            # 親のノードとしてquwに追加する
            que.put(i)

for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    elif color[c - 1] != color[d - 1]:
        print("Road")
