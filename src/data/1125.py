from collections import deque

N, Q = map(int, input().split())
nx = [[] for _ in range(N)]
for _ in range(N - 1):
    ai, bi = map(lambda s: int(s) - 1, input().split())
    nx[ai].append(bi)
    nx[bi].append(ai)

d = [-1] * N
d[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for nv in nx[v]:
        if d[nv] != -1:
            continue
        d[nv] = d[v] + 1
        q.append(nv)

for _ in range(Q):
    ci, di = map(lambda s: int(s) - 1, input().split())
    print('Town' if (d[ci] - d[di]) % 2 == 0 else 'Road')
