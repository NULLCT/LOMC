N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

from collections import deque

s = 0
todo = deque([s])
seen = [False] * N
seen[s] = True
color = [True] * N

while len(todo) > 0:
    tmp = todo.popleft()
    for i in G[tmp]:
        if seen[i] == False:
            seen[i] = True
            todo.append(i)
            color[i] = (not color[tmp])

for _ in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
