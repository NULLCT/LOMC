N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

stack = [(0, -1)]
C = [-1] * N
C[0] = 0
while stack:
    u, par = stack.pop()
    color = C[u]
    for v in G[u]:
        if v == par: continue
        stack.append((v, u))
        C[v] = color ^ 1

for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if C[c] == C[d]:
        print('Town')
    else:
        print('Road')
