from collections import defaultdict
from collections import deque

n, q = map(int, input().split())
ab = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab[a].append(b)
    ab[b].append(a)

visited = [False] * n
visited[0] = True
color = [0] * n
col = 0
que = {0}
while que:
    col = 1 - col
    nq = set()
    for x in que:
        for y in ab[x]:
            if visited[y]:
                continue
            color[y] = col
            visited[y] = True
            nq.add(y)
    que = nq

cc = [0] * q
dd = [0] * q
for i in range(q):
    cc[i], dd[i] = map(int, input().split())
for c, d in zip(cc, dd):
    c -= 1
    d -= 1
    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')