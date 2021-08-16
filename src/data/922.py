N, Q = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
visited = [-1 for _ in range(N)]
score = 0
visited[a] = score
queue = [a]
while queue:
    tmp = queue.pop()
    nexts = graph[tmp]
    score = (visited[tmp] + 1) % 2
    for item in nexts:
        if visited[item] == -1:
            queue.append(item)
            visited[item] = score
for _ in range(Q):
    c, d = list(map(int, input().split()))
    c, d = c - 1, d - 1
    if visited[c] == visited[d]:
        print("Town")
    else:
        print("Road")
