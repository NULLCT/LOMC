import queue

N, Q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

tmp = [0] * N
tmp[0] = 1

que = queue.Queue()
que.put(0)

while not que.empty():
    t = que.get()
    for i in G[t]:
        if tmp[i] == 0:
            tmp[i] = tmp[t] * (-1)
            que.put(i)

for i in range(Q):
    c, d = map(int, input().split())
    if tmp[c - 1] == tmp[d - 1]:
        print("Town")
    else:
        print("Road")