import queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()
que.put(0)
dist = [-1] * N
dist[0] = 0

while not que.empty():
    s = que.get()
    for i in G[s]:
        if dist[i] == -1:
            dist[i] = dist[s] + 1
            que.put(i)

for i in range(Q):
    c, d = map(int, input().split())
    if dist[c - 1] % 2 == dist[d - 1] % 2:
        print("Town")
    else:
        print("Road")
