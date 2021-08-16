import collections


def BSF(G, s):
    N = len(G)
    dist = [-1] * N
    que = collections.deque()

    dist[s] = 0
    que.append(s)

    while que:
        v = que.popleft()

        for i in G[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            que.append(i)

    return dist


N, Q = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(N - 1)]

G = []
for i in range(N):
    G.append(set())

for i in range(N - 1):
    G[AB[i][0] - 1].add(AB[i][1] - 1)
    G[AB[i][1] - 1].add(AB[i][0] - 1)

dist1 = BSF(G, 0)
M = max(dist1)
Mi = dist1.index(M)
dist2 = BSF(G, Mi)

for _ in range(Q):
    c, d = map(int, input().split())
    if (dist2[c - 1] + dist2[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
