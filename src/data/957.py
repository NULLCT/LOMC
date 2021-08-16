from collections import deque


def getdist(start):
    q = deque()
    q.append(start)
    dist[start] = 0

    while len(q) > 0:
        curr = q.popleft()
        for to in g[curr]:
            if dist[to] == 10**9:
                dist[to] = dist[curr] + 1
                q.append(to)


n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

dist = [10**9 for _ in range(n)]
getdist(0)

for _ in range(q):
    c, d = map(int, input().split())
    if abs(dist[c - 1] - dist[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
