N, Q = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
dis = [0 for _ in range(N)]
from collections import deque

q = deque()
q.append((0, 0))
seen = [False for _ in range(N)]
while q:
    now, t = q.popleft()
    seen[now] = True
    dis[now] = t
    for next in Edge[now]:
        if not seen[next]:
            q.append((next, t + 1))
for _ in range(Q):
    c, d = map(int, input().split())
    if (dis[c - 1] + dis[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
