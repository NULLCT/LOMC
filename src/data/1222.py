from collections import deque

N, Q = map(int, input().split())
E = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

d_from_1 = [None] * (N + 1)
que = deque([(1, 0, 0)])
for _ in range(N):
    v, p, d = que.popleft()
    d_from_1[v] = d
    for u in E[v]:
        if u != p:
            que.append((u, v, d + 1))

for _ in range(Q):
    c, d = map(int, input().split())
    dist = d_from_1[c] + d_from_1[d]
    if dist % 2 == 0:
        print('Town')
    else:
        print('Road')
