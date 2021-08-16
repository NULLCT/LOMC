from collections import deque

N, Q = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

D = [-1] * N
q = deque()
q.append((0, 0))
while q:
    a, d = q.popleft()
    D[a] = d

    for v in E[a]:
        if D[v] != -1:
            continue
        q.append((v, d + 1))

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(D[c] - D[d]) % 2:
        print('Road')
    else:
        print('Town')
