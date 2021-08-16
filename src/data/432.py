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
labels = [0 for x in range(N)]  # 0: ラベルなし, 1: even, -1: odd
labels[0] = 1

while not que.empty():
    current_node = que.get()
    current_label = labels[current_node]

    for next_node in graph[current_node]:
        if labels[next_node] == 0:
            que.put(next_node)
            labels[next_node] = -current_label

for query in queries:
    if labels[query[0]] * labels[query[1]] > 0:
        print("Town")
    else:
        print("Road")
