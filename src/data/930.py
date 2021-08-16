from collections import deque

n, Q = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
depth = [0] * n
que = deque([0])
check = [False] * n
check[0] = True
while que:
    q = que.popleft()
    for i in edge[q]:
        if not check[i]:
            check[i] = True
            que.append(i)
            depth[i] = depth[q] + 1
for i in range(Q):
    c, d = map(int, input().split())
    if (depth[c - 1] + depth[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
