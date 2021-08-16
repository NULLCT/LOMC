import queue

N, Q = map(int, input().split())

roads = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    roads[a - 1].append(b - 1)
    roads[b - 1].append(a - 1)

color = [-1] * N
color[0] = 0

que = queue.Queue()
que.put(0)

while not que.empty():
    cur = que.get()
    for next in roads[cur]:
        if color[next] == -1:
            color[next] = 0 if color[cur] else 1
            que.put(next)

for i in range(Q):
    c, d = map(int, input().split())
    print("Town" if color[c - 1] == color[d - 1] else "Road")
