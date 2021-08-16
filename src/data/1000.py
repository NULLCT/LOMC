import copy

N, Q = map(int, input().split())

tree = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

data = [[0, 0]]

Okinawa = 0
dist = 0
visited = [False] * N

while len(data) > 0:
    pos, depth = data.pop()
    visited[pos] = True
    if dist < depth:
        dist = copy.copy(depth)
        Okinawa = copy.copy(pos)
    for nxt in tree[pos]:
        if visited[nxt] == False:
            data.append([nxt, depth + 1])

data = [[Okinawa, 0]]

dist = [0] * N

visited = [False] * N

while len(data) > 0:
    pos, depth = data.pop()
    visited[pos] = True
    dist[pos] = depth
    for nxt in tree[pos]:
        if visited[nxt] == False:
            data.append([nxt, depth + 1])

for j in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if (dist[a] - dist[b]) % 2 == 0:
        print("Town")
    else:
        print("Road")
