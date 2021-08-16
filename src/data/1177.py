import collections

N, Q = map(int, input().split())
lsg = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    lsg[a].append(b)
    lsg[b].append(a)
# c,dの距離が偶数か奇数か
d = collections.deque([0])
used = [False] * (N)
lscost = [float('INF')] * (N)
lscost[0] = 0
while d:
    v = d.popleft()
    if used[v]:
        continue
    used[v] = True
    for j in lsg[v]:
        if used[j]:
            continue
        if lscost[j] > lscost[v] + 1:
            lscost[j] = lscost[v] + 1
            d.append(j)
lsQ = [map(int, input().split()) for i in range(Q)]
for i in range(Q):
    c, d = lsQ[i]
    c -= 1
    d -= 1
    if lscost[c] % 2 == lscost[d] % 2:
        print('Town')
    else:
        print('Road')
