n, q = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

group = [[], []]
town_color = [-1] * n
tmp = [[0, -1, 0]]
while tmp:
    v, past, color = tmp.pop()
    town_color[v] = color
    group[color].append(v + 1)
    for i in graph[v]:
        if i == past: continue
        tmp.append([i, v, color ^ 1])

# print(group[0])
# print(group[1])
# print(town_color)

for i in range(q):
    c, d = map(int, input().split())
    if town_color[c - 1] == town_color[d - 1]:
        print("Town")
    else:
        print("Road")
