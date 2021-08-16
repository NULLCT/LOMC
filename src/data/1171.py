from collections import deque

n, q = map(int, input().split())
e = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

depth = [-1] * n
depth[0] = 0
dq = deque([0])
while dq:
    x = dq.popleft()
    for v in e[x]:
        if depth[v] != -1:
            continue
        else:
            depth[v] = depth[x] + 1
            dq.append(v)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if depth[c] % 2 == depth[d] % 2:
        print('Town')
    else:
        print('Road')
