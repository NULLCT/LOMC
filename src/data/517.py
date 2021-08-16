from collections import defaultdict

graph = defaultdict(list)

n, q = map(int, input().split())

for i in range(1, n + 1):
    graph[i] = []

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = dict()

head = 1
queue = list()
queue.append((head, 1))
color[head] = 1
visited = set()
visited.add(head)

while queue:
    data = queue.pop(0)
    curr_node = data[0]
    curr_color = data[1]

    for node in graph[curr_node]:
        if node not in visited:
            visited.add(node)
            queue.append((node, 1 - curr_color))
            color[node] = 1 - curr_color

for i in range(q):
    a, b = map(int, input().split())

    if color[a] == color[b]:
        print("Town")
    else:
        print("Road")
