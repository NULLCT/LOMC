n, q = map(int, input().split())
link = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    link[a - 1].append(b - 1)
    link[b - 1].append(a - 1)
cd = [list(map(int, input().split())) for i in range(q)]

from collections import deque

visited = [-1] * n
visited[0] = True

from collections import deque

Q = deque()
Q.append(0)

while Q:
    now = Q.popleft()
    for nxt in link[now]:
        if visited[nxt] != -1:
            continue
        visited[nxt] = not visited[now]
        Q.append(nxt)

for c, d in cd:
    if visited[c - 1] == visited[d - 1]:
        print("Town")
    else:
        print("Road")
