from collections import deque

N, Q = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = [i - 1 for i in list(map(int, input().split()))]
    edges[a].append(b)
    edges[b].append(a)

d = [-1 for _ in range(N)]
d[0] = 0
que = deque([0])
while que:
    t = que.popleft()
    for to in edges[t]:
        if d[to] == -1:
            d[to] = d[t] ^ 1
            que.append(to)

for i in range(Q):
    a, b = [i - 1 for i in list(map(int, input().split()))]
    if d[a] == d[b]:
        print("Town")
    else:
        print("Road")
