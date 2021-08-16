import queue

N, Q = map(int, input().split())

AB_2d = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    AB_2d[A - 1].append(B - 1)
    AB_2d[B - 1].append(A - 1)

Q_2d = [list(map(int, input().split())) for _ in range(Q)]

que = queue.Queue()
color = [-1] * N
color[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in AB_2d[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)

for q in Q_2d:
    if color[q[0] - 1] == color[q[1] - 1]:
        print("Town")
    else:
        print("Road")
