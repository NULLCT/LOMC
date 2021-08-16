from collections import deque

N, Q = map(int, input().split())

R = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    R[a].append(b)
    R[b].append(a)

D = [-1] * N
D[0] = 0
queue = deque([0])
while queue:
    nxt = queue.popleft()
    for i in R[nxt]:
        if D[i] == -1:
            queue.append(i)
            D[i] = D[nxt] + 1

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if b > a:
        a, b = b, a
    if (D[a] - D[b]) % 2 == 0:
        print("Town")
    else:
        print("Road")
