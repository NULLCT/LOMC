from collections import deque


def bfs(G):
    queue = deque([0])
    P = [-1] * len(G)
    P[0] = 0
    while queue:
        node = queue.popleft()
        for n in G[node]:
            if P[n] != -1:
                continue
            P[n] = (P[node] + 1) % 2
            queue.append(n)
    return P


n, q = list(map(int, input().split()))
G = [set() for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    G[u - 1].add(v - 1)
    G[v - 1].add(u - 1)
P = bfs(G)

for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if (P[u] + P[v]) % 2 == 1:
        print('Road')
    else:
        print('Town')
