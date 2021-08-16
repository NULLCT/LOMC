from collections import deque

N, Q = map(int, input().split())
e = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    e[a - 1].append(b - 1)
    e[b - 1].append(a - 1)

q = deque()
dst = [-1] * N
q.append(0)
dst[0] = 0
while q:
    now = q.popleft()
    for nxt in e[now]:
        if dst[nxt] == -1:
            dst[nxt] = dst[now] + 1
            q.append(nxt)

for _ in range(Q):
    c, d = map(int, input().split())
    if (dst[c - 1] + dst[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
