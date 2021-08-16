from collections import deque

N, Q = map(int, input().split())
edges = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
data = []
for i in range(Q):
    x = list(map(int, input().split()))
    data.append(x)
inf = float("inf")


def search(edge):
    dist = [inf] * (N + 1)
    dist[1] = 0
    m = deque()
    for i in edge[1]:
        m.append(i)
        dist[i] = 1
    while len(m):
        a = m.popleft()
        for i in edge[a]:
            if dist[i] == inf:
                if dist[a] == 1:
                    dist[i] = 0
                else:
                    dist[i] = 1
                m.append(i)
    return dist


D = search(edges)
for i in range(Q):
    c, d = data[i][0], data[i][1]
    c1 = D[c]
    d1 = D[d]
    if c1 == d1:
        print("Town")
    else:
        print("Road")
