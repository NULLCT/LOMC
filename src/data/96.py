from collections import deque


def bfs(graph, N):
    parities = [None] * N
    parities[0] = 0
    que = deque([0])
    while que:
        node = que.popleft()
        p = parities[node] ^ 1
        for n in graph[node]:
            if parities[n] is None:
                parities[n] = p
                que.append(n)
    return parities


N, _, *R = map(int, open(0).read().split())
M = 2 * (N - 1)
R = [r - 1 for r in R]
E = R[:M]
Q = R[M:]
graph = [[] for _ in range(N)]
for a, b in zip(E[::2], E[1::2]):
    graph[a].append(b)
    graph[b].append(a)
parities = bfs(graph, N)
for a, b in zip(Q[::2], Q[1::2]):
    print("TRoowand"[parities[a] ^ parities[b]::2])
