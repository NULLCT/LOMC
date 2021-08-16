N, Q = map(int, input().split())
T = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    T[a].append(b)
    T[b].append(a)

depth = [0] * N
visited = [0] * N
stack = [0]
while stack:
    n = stack.pop()
    if visited[n]:
        continue
    visited[n] = 1

    for to in T[n]:
        if visited[to]:
            continue
        depth[to] = depth[n] + 1
        stack.append(to)

for i in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    diff = abs(depth[c] - depth[d])
    print('Road' if diff % 2 == 1 else 'Town')
