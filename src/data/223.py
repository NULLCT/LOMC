from queue import Queue

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

color = [None] * N
queue = Queue()
color[0] = 0
queue.put(0)
while not queue.empty():
    t = queue.get()
    for s in G[t]:
        if color[s] is None:
            color[s] = 1 - color[t]
            queue.put(s)

for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
