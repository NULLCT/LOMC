import queue

n, q = map(int, input().split())

edge = {}
for i in range(n):
    edge[i] = []

for i in range(n - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

# print(edge)

color = [-1 for i in range(n)]
color[0] = 0

visited = [False for i in range(n)]

# def dfs(v, even):
#     visited[v] = True

#     if even:
#         even_v[v] = True

#     for w in edge[v]:
#         if not visited[w]:
#             dfs(w, not even)

# dfs(0, True)

que = queue.Queue()
que.put(0)

while not que.empty():
    v = que.get()

    for w in edge[v]:
        if color[w] == -1:
            color[w] = 1 - color[v]
            que.put(w)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
