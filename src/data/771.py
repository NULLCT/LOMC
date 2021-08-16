import collections

D = collections.defaultdict(list)

N, Q = map(int, input().split())
for i in range(N - 1):
    a, b = map(int, input().split())
    D[a].append(b)
    D[b].append(a)

edge = []
for i in range(Q):
    c, d = map(int, input().split())
    edge.append([c, d])

#前処理
dist = [-1] * (N + 1)
dist[0] = 0
dist[1] = 0

queue = collections.deque()
queue.append(1)

while queue:
    v = queue.popleft()
    for i in D[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        queue.append(i)

for i in range(Q):
    takahashi = edge[i][0]
    aoki = edge[i][1]

    if (dist[takahashi] - dist[aoki]) % 2 == 0:
        print("Town")
    else:
        print("Road")
