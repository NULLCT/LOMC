from collections import deque

N, Q = map(int, input().split())
T = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    T[a - 1].append(b - 1)
    T[b - 1].append(a - 1)

D = [-1] * N
que = deque([0])
D[0] = 0
while que:
    s = que.pop()

    for to in T[s]:
        if D[to] != -1:
            continue
        D[to] = D[s] + 1
        que.append(to)

for _ in range(Q):
    c, d = map(int, input().split())
    if abs(D[c - 1] - D[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
