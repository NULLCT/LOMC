import queue

N, Q = map(int, input().split())

G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()
color = [-1] * N
color[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for n in G[t]:
        if color[n] == -1:
            if color[t] == 0:
                color[n] = 1
            else:
                color[n] = 0
            que.put(n)

for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
