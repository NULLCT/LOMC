from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * N

start = 0
q = deque()
q.append(0)
visited[start] = 0

while q:

    now = q.popleft()

    for next in graph[now]:
        if visited[next] != -1:
            continue

        q.append(next)
        visited[next] = visited[now] + 1

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    if (visited[c] - visited[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
