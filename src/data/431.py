import queue

N, Q = [int(x) for x in input().split()]

graph = [[] for i in range(N)]
for i in range(N - 1):
    a, b = [int(x) for x in input().split()]
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

queries = []
for i in range(Q):
    c, d = [int(x) for x in input().split()]
    queries.append([c - 1, d - 1])

que = queue.Queue()
que.put(0)
distances = [-1 for x in range(N)]  # 0: ラベルなし, 1: even, -1: odd
distances[0] = 0

while not que.empty():
    current_node = que.get()
    current_distance = distances[current_node]

    for next_node in graph[current_node]:
        if distances[next_node] < 0:
            que.put(next_node)
            distances[next_node] = current_distance + 1

for query in queries:
    if (distances[query[0]] - distances[query[1]]) % 2 == 0:
        print("Town")
    else:
        print("Road")
