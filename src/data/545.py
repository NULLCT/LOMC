import math

n, q = map(int, input().split())

# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
ab = [[] for i in range(n + 1)]

for i in range(0, n - 1):
    a_t, b_t = map(int, input().split())
    ab[a_t].append(b_t)
    ab[b_t].append(a_t)

import queue

que = queue.Queue()
color = [-1] * (n + 1)
color[1] = 0

que.put(1)

# すべてにカラーをつける
# 二部グラフ
# すべての道に到達できる前提だから、これですべてに色をつけられる
while not que.empty():
    t = que.get()
    for i in ab[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)

for i in range(0, q):
    c_t, d_t = map(int, input().split())
    if color[c_t] == color[d_t]:
        print("Town")
    else:
        print("Road")
