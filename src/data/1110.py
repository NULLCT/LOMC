from collections import deque

N, Q = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = [-1 for i in range(N)]

d = deque([0])
ans[0] = 0
while d:
    i = d.pop()

    for j in graph[i]:
        if ans[j] == -1:
            ans[j] = (ans[i] + 1) % 2
            d.append(j)

for i in range(Q):
    c, d = map(int, input().split())
    if ans[c - 1] == ans[d - 1]:
        print('Town')
    else:
        print('Road')
