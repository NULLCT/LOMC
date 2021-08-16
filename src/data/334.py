import sys

sys.setrecursionlimit(10**6)
ml = lambda: list(map(int, input().split()))
mp = lambda: map(int, input().split())

N, Q = mp()
edge = list([] for _ in range(N))
dist = [-1] * N
visited = [0] * N
for i in range(N - 1):
    a, b = mp()
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

q = [0]
visited[0] = 1
dist[0] = 0
while q:
    now = q.pop()
    for next in edge[now]:
        if not visited[next]:
            visited[next] = 1
            dist[next] = dist[now] + 1
            q.append(next)

for i in range(Q):
    c, d = mp()
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
