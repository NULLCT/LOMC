import queue

N, Q = map(int, input().split())
paths = []
for n in range(N - 1):
    a, b = map(int, input().split())
    paths.append((a, b))
queries = []
for q in range(Q):
    a, b = map(int, input().split())
    queries.append((a, b))

graph = [[] for _ in range(N)]
for path in paths:
    a, b = path
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

color = [-1] * N
color[0] = 0
q = queue.Queue()
q.put(0)
while not q.empty():
    p = q.get()
    for i in graph[p]:
        if color[i] == -1:
            color[i] = 1 - color[p]
            q.put(i)
for q in queries:
    a, b = q
    if color[a - 1] == color[b - 1]:
        print("Town")
    else:
        print("Road")
