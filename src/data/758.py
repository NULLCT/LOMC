#幅優先探索
n, Q = map(int, input().split())
m = n - 1
e = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    e[a].append(b)
    e[b].append(a)

que = [0]
visited = [0] * n
dist = [0] * n
visited[0] = 1
while len(que):
    q = que.pop(0)
    d = dist[q] + 1
    for i in e[q]:
        if visited[i] == 0:
            visited[i] = 1
            dist[i] = d
            que.append(i)

for i in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if abs(dist[a] - dist[b]) % 2 == 0:
        print('Town')
    else:
        print('Road')
