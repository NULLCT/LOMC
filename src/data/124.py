from collections import deque

N, q = map(int, input().split())
X = [[] for i in range(N)]
for i in range(N - 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    X[x].append(y)
    X[y].append(x)

P = [-1] * N
Q = deque([0])
R = []
D = [0] * N
while Q:
    i = deque.popleft(Q)
    R.append(i)
    for a in X[i]:
        if a != P[i]:
            P[a] = i
            D[a] = D[i] ^ 1
            X[a].remove(i)
            deque.append(Q, a)

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    print("Road" if D[c] ^ D[d] else "Town")
