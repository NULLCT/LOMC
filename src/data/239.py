from collections import deque

N, Q = map(int, input().split())
arrAB = [list(map(int, input().split())) for i in range(N - 1)]
arrCD = [list(map(int, input().split())) for i in range(Q)]

grp = [[] for i in range(N)]
for a, b in arrAB:
    grp[a - 1].append(b - 1)
    grp[b - 1].append(a - 1)

que = deque([])
dist = [-1] * N
dist[0] = 0
que.append(0)

while len(que) > 0:
    v = que.popleft()
    for next_v in grp[v]:
        if dist[next_v] != -1:
            continue

        dist[next_v] = dist[v] + 1
        que.append(next_v)

for c, d in arrCD:
    l1 = dist[c - 1]
    l2 = dist[d - 1]
    if (l1 + l2) % 2 == 0:
        print("Town")
    else:
        print("Road")
