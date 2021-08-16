N, Q = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

from collections import deque

dq = deque()
dq.append([0, 0])
D = [-1] * N
while dq:
    u, d = dq.popleft()
    D[u] = d
    for v in G[u]:
        if D[v] == -1:
            dq.append([v, d + 1])

for _ in range(Q):
    c, d = list(map(lambda x: int(x) - 1, input().split()))
    if (D[c] - D[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
