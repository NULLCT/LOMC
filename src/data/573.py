import queue

n, q = map(int, input().split())
G = [[] for i in range(n)]

for i in range(n - 1):
    ind = lambda n: int(n) - 1
    a, b = map(ind, input().split())
    G[a].append(b)
    G[b].append(a)

que = queue.Queue()
color = [-1 for _ in range(n)]
color[0] = 0
que.put(0)

while not que.empty():
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)

for i in range(q):
    ind = lambda n: int(n) - 1
    a, b = map(ind, input().split())
    print('Town' if color[a] == color[b] else 'Road')
