N, Q = map(int, input().split())
roads = [[] for _ in range(N + 1)]
queries = []

for _ in range(N - 1):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

for _ in range(Q):
    queries.append(tuple(map(int, input().split())))

binary_map = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
visited[1] = True
stack = [1]

while len(stack) > 0:
    begin = stack.pop()
    for end in roads[begin]:
        if visited[end]:
            continue
        visited[end] = True
        binary_map[end] = binary_map[begin] ^ 1
        stack.append(end)

for c, d in queries:
    if binary_map[c] == binary_map[d]:
        print("Town")
    else:
        print("Road")
