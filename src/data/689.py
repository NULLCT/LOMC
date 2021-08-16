import queue

N, Q = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()
dist_mod = [-1] * N
dist_mod[0] = 0
que.put(0)

while not que.empty():
    t = que.get()
    for i in G[t]:
        if dist_mod[i] == -1:
            dist_mod[i] = 1 - dist_mod[t]
            que.put(i)

for i in range(Q):
    c, d = map(int, input().split())
    if dist_mod[c - 1] == dist_mod[d - 1]:
        print("Town")
    else:
        print("Road")
