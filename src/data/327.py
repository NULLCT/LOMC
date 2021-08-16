N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

color = [-1] * N
stack = [0]
color[0] = 0
while stack:
    from_ = stack.pop()
    for to in edge[from_]:
        if (color[to] != -1):
            continue
        color[to] = color[from_] ^ 1
        stack.append(to)

for _ in range(Q):
    c, d = map(int, input().split())
    if (color[c - 1] == color[d - 1]):
        print("Town")
    else:
        print("Road")
