import queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

q = queue.Queue()
color = [-1] * N
color[0] = 0
q.put(0)
while not q.empty():
    t = q.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            q.put(i)

for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
