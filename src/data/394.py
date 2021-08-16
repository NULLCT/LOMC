n, q = map(int, input().split())
connected = {i: [] for i in range(n)}

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    connected[a].append(b)
    connected[b].append(a)

que = [(-1, 0, 0)]  # previous, now, color
colors = [-1] * n

while len(que) >= 1:
    prev, pos, col = que.pop()
    colors[pos] = col
    next_town = [t for t in connected[pos] if t != prev]
    next_col = (col + 1) % 2
    for t in next_town:
        que.append((pos, t, next_col))

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1

    if colors[c] == colors[d]:
        print('Town')
    else:
        print('Road')
