# 深さで塗り分けする→偶奇判定が答え
from collections import deque

n, Q = map(int, input().split())
adj = [[] for i in range(n + 1)]
for i in range(1, n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# paint
q = deque([(a, 1)])
color = [-1] * (n + 1)

while q:
    c, paint = q.popleft()
    for i in adj[c]:
        if color[i] != -1:
            continue
        else:
            color[i] = paint
            q.append((i, (paint + 1) % 2))

for i in range(Q):
    c, d = map(int, input().split())
    if color[c] != color[d]:
        print('Road')
    else:
        print('Town')
