from collections import deque

n, q = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
que = deque([0])
d = [-1] * n
d[0] = 0
while que:
    x = que.popleft()
    for nx in edge[x]:
        if d[nx] != -1:
            continue
        d[nx] = d[x] + 1
        que.append(nx)
for _ in range(q):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    if (d[ci] + d[di]) % 2:
        print("Road")
    else:
        print("Town")
