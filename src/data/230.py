import queue

n, q = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()
color = [-1] * n
color[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)

for i in range(q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print('Town')
    else:
        print('Road')
