from collections import deque

N, Q = map(int, input().split())

G = []
for i in range(N):
    G.append([])

for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

dist = []
for i in range(N):
    dist.append(-1)

s = 0
q = deque()
q.append(s)
dist[s] = 0

while len(q) > 0:
    i = q.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            q.append(j)

for i in range(Q):
    C, D = map(int, input().split())
    C -= 1
    D -= 1
    temp = dist[C] + dist[D]
    if temp % 2 == 0:
        print("Town")
    else:
        print("Road")
