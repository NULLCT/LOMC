N, Q = map(int, input().split())
tree = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

color = [-1] * N
color[0] = 0
stack = [(0, -1)]
while stack:
    node, par = stack.pop()
    c = 1 - color[node]
    for child in tree[node]:
        if child == par:
            continue

        color[child] = c
        stack.append((child, node))

ans = []
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if color[c] == color[d]:
        ans.append('Town')
    else:
        ans.append('Road')

print(*ans, sep='\n')
