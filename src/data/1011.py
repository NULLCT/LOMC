N, Q = map(int, input().split())
Tree = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    Tree[a - 1].append(b - 1)
    Tree[b - 1].append(a - 1)

stack = [(0, 0)]
color = [-1 for _ in range(N)]
while len(stack) != 0:
    x, c = stack.pop()
    if color[x] != -1:
        continue

    for p in Tree[x]:
        if c == 0:
            stack.append((p, 1))
        else:
            stack.append((p, 0))

    color[x] = c

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')
