import queue

n, q = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

que = queue.Queue()
color = [0] * n
color[0] = 1
que.put(0)

while not que.empty():
    t = que.get()
    for i in g[t]:
        if color[i] == 0:
            color[i] = -color[t]
            que.put(i)

for i in range(q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print('Town')
    else:
        print('Road')
