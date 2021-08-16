import queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()

serch = [-1] * N
serch[0] = 0
que.put(0)

while not que.empty():
    t = que.get()
    for i in G[t]:
        if serch[i] == -1:
            serch[i] = 1 - serch[t]
            que.put(i)

for i in range(Q):
    c, d = map(int, input().split())
    if serch[c - 1] == serch[d - 1]:
        print("Town")
    else:
        print("Road")
