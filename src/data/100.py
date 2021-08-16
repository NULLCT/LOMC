N, q = map(int, input().split())
adj = [[] for _ in range(N)]
dist = [0] * N
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

start = 0
visited = {start}
Q = [start]

while Q:
    cur = Q.pop()
    for nex in adj[cur]:
        if nex in visited:
            continue
        else:
            visited.add(nex)
            dist[nex] = (dist[cur] + 1) % 2
            Q.append(nex)

for _ in range(q):
    a, b = map(lambda x: int(x) - 1, input().split())
    if dist[a] == dist[b]:
        print("Town")
    else:
        print("Road")
