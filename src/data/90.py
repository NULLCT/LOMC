N, Q = map(int, input().split())

G = [None] + [[] for _ in range(N)]
C = [None] * (N + 1)
C[1] = 1

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[b].append(a)
    G[a].append(b)

s = [1]

while s:
    u = s.pop()
    for v in G[u]:
        if C[v] is None:
            s.append(v)
            C[v] = C[u] ^ 1

for _ in range(Q):
    c, d = map(int, input().split())
    print('Road' if C[c] ^ C[d] else 'Town')
