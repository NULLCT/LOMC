from collections import deque

n, q = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b)
    g[b - 1].append(a)

#0, 1に採色
start = 1
color = [-1 for _ in range(n)]  #dist
color[start - 1] = 0
todo = deque([start])
seen = deque()

while len(todo) > 0:
    seek = todo.popleft()
    seen.append(seek)

    for v in g[seek - 1]:
        if color[v - 1] == -1:
            color[v - 1] = 1 - color[seek - 1]
            todo.append(v)

for _ in range(q):
    c, d = map(int, input().split())

    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
