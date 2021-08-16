from collections import deque

N, Q = map(int, input().split())

ranklst = [-1] * N
ranklst[0] = 0
edges = []

for i in range(N):
    edges.append([])

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

d = deque()
d.append(0)
while d:
    now = d.popleft()
    nowrank = ranklst[now]
    for i in edges[now]:
        if ranklst[i] == -1:
            ranklst[i] = nowrank + 1
            d.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if ranklst[c] % 2 == ranklst[d] % 2:
        ans = 'Town'
    else:
        ans = 'Road'

    print(ans)
