import queue

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
que = queue.Queue()
cd = [list(map(int, input().split())) for _ in range(q)]

colour = [0] + [-1] * (n - 1)
que.put(0)

while not que.empty():
    t = que.get()
    for i in g[t]:
        if colour[i] == -1:
            colour[i] = 1 - colour[t]
            que.put(i)
for i in range(q):
    if colour[cd[i][0] - 1] == colour[cd[i][1] - 1]:
        print('Town')
    else:
        print('Road')
