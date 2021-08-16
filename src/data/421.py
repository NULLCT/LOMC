import queue

N, Q = map(int, input().split())
G = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
que = queue.Queue()
color = [-1] * (N + 1)
color[1] = 0
que.put(1)
while not que.empty():
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)
for t in range(Q):
    a, b = map(int, input().split())
    if color[a] == color[b]:
        print("Town")
    else:
        print("Road")
