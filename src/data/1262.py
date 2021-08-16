from collections import deque

n, q = map(int, input().split())
ab = []
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ab.append([a - 1, b - 1])
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
visited = [-1 for i in range(n)]
visited[ab[0][0]] = 0
que = deque()
que.append(ab[0][0])
while que:
    x = que.popleft()
    for i in edge[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            que.append(i)
        else:
            continue
#print(visited)
for i in range(q):
    c, d = map(int, input().split())
    if (visited[c - 1] + visited[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
