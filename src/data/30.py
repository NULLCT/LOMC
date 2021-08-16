from queue import Queue

N, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
queries = [list(map(int, input().split())) for _ in range(Q)]

edges_from = dict.fromkeys([i for i in range(1, N + 1)])

for vertex in edges_from.keys():
    edges_from[vertex] = []

for edge in edges:
    a = edge[0]
    b = edge[1]

    edges_from[a].append(b)
    edges_from[b].append(a)

vertex_waitlist = Queue()
visited = [-1 for _ in range(N + 1)]  # -1 = not visited, 0 = even, 1 = odd

vertex_waitlist.put(1)
visited[1] = 0

while not vertex_waitlist.empty():
    vertex = vertex_waitlist.get()

    for next_vertex in edges_from[vertex]:
        if visited[next_vertex] != -1:
            continue

        vertex_waitlist.put(next_vertex)
        visited[next_vertex] = (visited[vertex] +
                                1) % 2  # flip between 0 and 1

for query in queries:
    c = query[0]
    d = query[1]

    if visited[c] == visited[d]:
        print("Town")
    else:
        print("Road")
