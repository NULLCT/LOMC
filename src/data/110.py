import queue

n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

color = [-1] * n
color[0] = 0
que = queue.Queue()
que.put(0)

while not que.empty():
    t = que.get()

    for i in g[t]:
        if color[i] != -1:
            continue

        color[i] = 1 - color[t]
        que.put(i)

for i in range(q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print('Town')
    else:
        print('Road')
