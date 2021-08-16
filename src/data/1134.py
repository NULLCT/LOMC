from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def bfs(x):
    d = [-1] * N
    d[x] = 0
    queue = deque([x])
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if d[y] < 0:
                d[y] = d[x] + 1
                queue.append(y)
    return d


ans = bfs(1)
for i in range(Q):
    c, d = map(int, input().split())
    if abs(ans[c - 1] - ans[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
