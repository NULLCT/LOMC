from collections import defaultdict, deque

N, Q = map(int, input().split())
info = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    info[a].append(b)
    info[b].append(a)
dist = [-1] * N
dist[0] = 0
que = deque([(0, 0)])
while que:
    d, c = que.popleft()
    for to in info[c]:
        if dist[to] != -1:
            continue
        dist[to] = d + 1
        que.append((d + 1, to))

for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    ans = "Town" if dist[c] % 2 == dist[d] % 2 else "Road"
    print(ans)
