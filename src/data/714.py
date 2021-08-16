N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
D = [-1] * N
D[0] = 0
q = [0]
for u in q:
    for v in G[u]:
        if D[v] >= 0:
            continue
        D[v] = D[u] ^ 1
        q.append(v)
for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if D[u] == D[v]:
        print("Town")
    else:
        print("Road")
