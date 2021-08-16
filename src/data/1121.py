from collections import defaultdict  # , deque
from heapq import heappop, heappush

INF = 1 << 60
E = defaultdict(list)
n, q = map(int, input().split())
for _ in range(n - 1):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    E[i].append(j)
    E[j].append(i)
dist = [INF] * n
# que = deque([0])
que = [(0, 0)]
dist[0] = 0
while que:
    _, v = heappop(que)  # que.popleft()
    for u in E[v]:
        # if dist[u] == INF:
        #    que.append(v)
        if dist[u] > dist[v] + 1:
            dist[u] = dist[v] + 1
            heappush(que, (dist[u], u))
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
