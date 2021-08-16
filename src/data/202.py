N, Q = map(int, input().split())

arr = {i: [] for i in range(N + 1)}

for i in range(1, N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

color = [-1] * (N + 1)
color[1] = 1
que = []
que.append(1)

while que:
    t = que.pop(0)
    for i in arr[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.append(i)

for _ in range(Q):
    a, b = map(int, input().split())
    if color[a] == color[b]:
        print('Town')
    else:
        print('Road')