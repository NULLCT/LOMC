from collections import deque

N, Q = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

todo = deque([1])
seen = [-1] * (N + 1)
seen[1] = 0
while todo:
    v = todo.pop()
    for next in G[v]:
        if seen[next] == -1:
            seen[next] = seen[v] + 1
            todo.append(next)

for i in range(Q):
    c, d = map(int, input().split())
    if (seen[c] - seen[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
