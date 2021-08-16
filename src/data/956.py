from collections import deque

n, Q = map(int, input().split())
l = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    l[a].append(b)
    l[b].append(a)
vis = [-1] * n
vis[0] = 0
q = deque([[0, 0]])
while q:
    node, cnt = q.popleft()
    for nd in l[node]:
        if vis[nd] == -1:
            vis[nd] = (cnt + 1) & 1
            q.append([nd, cnt + 1])
for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if vis[c] ^ vis[d]:
        print("Road")
    else:
        print("Town")
