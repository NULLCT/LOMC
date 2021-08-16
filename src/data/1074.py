from collections import deque

N, Q = map(int, input().split())
e = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    e[a].append(b)
    e[b].append(a)
cd = [list(map(int, input().split())) for _ in range(Q)]

flag = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

q = deque()
q.append([1, 1])  #[街番号, flag]
flag[1] = 1

while q:
    t, f = q.popleft()
    if visited[t]:
        continue
    visited[t] = 1
    if f:
        flag[t] = 1
    else:
        flag[t] = 0
    for v in e[t]:
        if f:
            q.append([v, 0])
        else:
            q.append([v, 1])

for c, d in cd:
    if flag[c] == flag[d]:
        print("Town")
    else:
        print("Road")
