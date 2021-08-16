N, C = map(int, input().split())
M = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    M[a].append(b)
    M[b].append(a)

from collections import deque

Q = deque()
path = [0 for i in range(N + 1)]
color = [0 for i in range(N + 1)]
Q.append(1)
while (len(Q) > 0):
    q = Q.popleft()
    color[q] = 1
    for item in M[q]:
        if (color[item] == 0):
            Q.append(item)
            path[item] = path[q] + 1

for _ in range(C):
    a, b = map(int, input().split())
    if ((path[a] + path[b]) % 2 == 0):
        print("Town")
    else:
        print("Road")
