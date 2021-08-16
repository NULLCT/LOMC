from collections import deque

N, Q = map(int, input().split())
T = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    T[a].append(b)
    T[b].append(a)

q = deque([(0, 0)])
used = [0] * N
C = [0] * N
while q:
    a, b = q.popleft()
    used[a] = 1
    for i in T[a]:
        if used[i] == 0:
            used[i] = 1
            C[i] = b + 1
            q.append((i, b + 1))

for i in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if abs(C[c] - C[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")