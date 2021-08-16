from collections import deque

N, Q = map(int, input().split())
E = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
D = [0] * (N + 1)
V = [0] * (N + 1)
V[1] = 1
P = deque([1])
while P:
    x = P[0]
    for y in E[x]:
        if V[y] == 0:
            P.append(y)
            V[y] = 1
            D[y] = D[x] + 1
    P.popleft()
for q in range(Q):
    c, d = map(int, input().split())
    if abs(D[c] - D[d]) % 2 == 1:
        print('Road')
    else:
        print('Town')
