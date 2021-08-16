from collections import defaultdict

N, Q = map(int, input().split())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queries = []

for _ in range(Q):
    c, d = map(int, input().split())
    queries.append([c, d])

visited = defaultdict(bool)
distances = defaultdict(int)

queue = [1]
visited[1] = True
distances[1] = 0

while len(queue) > 0:
    current_node = queue.pop(0)

    for node in graph[current_node]:
        if visited[node]:
            continue
        visited[node] = True
        distances[node] = distances[current_node] + 1
        queue.append(node)

for query in queries:
    if (distances[query[0]] - distances[query[1]]) % 2 == 0:
        print("Town")
    else:
        print("Road")
