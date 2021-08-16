N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
cd = [list(map(int, input().split())) for _ in range(Q)]

path = [list() for _ in range(N + 1)]
for p in ab:
    path[p[0]].append(p[1])
    path[p[1]].append(p[0])

state = [-1] * (N + 1)

from collections import deque

q = deque()
q.append(1)

state[1] = 0

while len(q) > 0:
    now = q.popleft()

    for i in path[now]:
        if state[i] == -1:
            state[i] = (state[now] + 1) % 2
            q.append(i)

for query in cd:
    start = query[0]
    goal = query[1]
    if state[start] == state[goal]:
        print("Town")
    else:
        print("Road")
