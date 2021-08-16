N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

color = [None for _ in range(N)]
color[0] = 0
stack = [0]
while stack:
    v = stack.pop()
    nc = int(not color[v])
    for nv in E[v]:
        if color[nv] == None:
            color[nv] = nc
            stack.append(nv)

for _ in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
