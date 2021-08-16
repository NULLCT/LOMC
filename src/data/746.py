import queue

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
dist = [100000000 for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

que = queue.Queue()
que.put((0, 0))
while not que.empty():
    p, c = que.get()
    if dist[p] == 100000000:
        dist[p] = c
        for e in graph[p]:
            que.put((e, c + 1))

for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
