n, q = map(int, input().split())
ed = [list() for i in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    ed[a].append(b)
    ed[b].append(a)


def BFS(edge, s):
    from collections import deque

    dist = [-1] * n
    dist[s] = 0

    q = deque()
    q.append(s)

    while q:
        v = q.popleft()
        for i in edge[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            q.append(i)

    return dist


ds = BFS(ed, 0)
for i in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if abs(ds[c] - ds[d]) % 2:
        print("Road")
    else:
        print("Town")
