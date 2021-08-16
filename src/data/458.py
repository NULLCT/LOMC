from queue import Queue
import math

N, Q = map(int, input().split())
AB = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N - 1)]
CD = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]
graph = [[] for _ in range(N)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)

queue = Queue()
queue.put(0)
colors = [None for _ in range(N)]
colors[0] = 0

while not queue.empty():
    v = queue.get()
    for adj in graph[v]:
        if colors[adj] is None:
            if colors[v] == 0:
                colors[adj] = 1
            elif colors[v] == 1:
                colors[adj] = 0
            queue.put(adj)

for c, d in CD:
    if colors[c] == colors[d]:
        print("Town")
    else:
        print("Road")
