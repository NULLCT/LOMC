import queue

N, Q = (int(x) for x in input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = (int(x) for x in input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

color = [-1] * N
color[0] = 0
todo = queue.Queue()
todo.put(0)
while not todo.empty():
    v = todo.get()
    for i in G[v]:
        if color[i] == -1:
            color[i] = 1 - color[v]
            todo.put(i)

for _ in range(Q):
    c, d = (int(x) for x in input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
