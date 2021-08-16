import queue

N, Q = map(int, input().split())
g = [[] * N for i in range(N)]
for _ in range(N - 1):
    i, j = map(int, input().split())
    g[i - 1].append(j - 1)
    g[j - 1].append(i - 1)

que = queue.Queue()
color = [-1] * N
color[0] = 0

que.put(0)
while not que.empty():
    t = que.get()
    for i in g[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)

for _ in range(Q):
    i, j = map(int, input().split())
    if color[i - 1] == color[j - 1]:
        print("Town")
    else:
        print("Road")
