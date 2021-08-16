from collections import deque

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

inf = 10**24


def BFS(s):
    cost = [inf] * n
    cost[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in g[x]:
            if cost[y] == inf:
                cost[y] = cost[x] + 1
                q.append(y)
    return cost


cost = BFS(0)
for _ in range(q):
    c, d = map(int, input().split())
    if (cost[c - 1] + cost[d - 1]) % 2:
        print('Road')
    else:
        print('Town')
