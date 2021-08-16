from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def bfs(s):
    cost = [float("inf")] * n
    cost[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in graph[x]:
            if cost[y] > cost[x] + 1:
                cost[y] = cost[x] + 1
                q.append(y)
    return cost


cost = bfs(0)

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    ans = abs(cost[c] - cost[d])
    if ans % 2:
        print("Road")
    else:
        print("Town")
