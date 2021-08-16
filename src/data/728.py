#n = int(input())
#s = input()
n, q = map(int, input().split())
# = list(map(int, input().split()))
#ab = [list(map(int, input().split())) for _ in range(n-1)]

from collections import deque

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

ans = dist[1:]
#print(ans)

cd = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    c = cd[i][0] - 1

    d = cd[i][1] - 1
    if ans[c] % 2 == ans[d] % 2:
        print('Town')
    else:
        print('Road')
