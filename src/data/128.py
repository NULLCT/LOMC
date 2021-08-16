n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda a: int(a) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
stack = [0]
color = [0] * n
color[0] = 1
while stack:
    u = stack.pop()
    for v in g[u]:
        if color[v] > 0:
            continue
        color[v] = 3 - color[u]
        stack.append(v)
for _ in range(q):
    c, d = map(lambda a: int(a) - 1, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")