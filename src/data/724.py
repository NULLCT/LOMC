from collections import deque


def bfs():
    seen = [False] * n
    q = deque()
    q.append([0, 0])
    d_list = [0] * n
    while q:
        now, dist = q.popleft()
        if seen[now]:
            continue
        seen[now] = True
        d_list[now] = dist
        for node in edge[now]:
            q.append([node, dist + 1])
    return d_list


n, q = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

d_list = bfs()

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(d_list[c] - d_list[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
