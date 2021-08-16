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
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)
for i in range(Q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print('Town')
    else:
        print('Road')
