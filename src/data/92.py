n, q = map(int, input().split())
edges = {}
visited = {}
for i in range(1, n + 1):
    edges[i] = []
    visited[i] = -1
for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

from collections import deque


def bfs(edges, root):
    global visited
    que = deque()
    que.append(root)
    visited[root] = 0
    while que:
        x = que.popleft()
        for y in edges[x]:
            if visited[y] == -1:
                que.append(y)
                visited[y] = visited[x] + 1


bfs(edges, 1)
for i in range(q):
    x, y = map(int, input().split())
    if (visited[x] + visited[y]) % 2 == 0:
        print('Town')
    else:
        print('Road')
