from collections import deque

N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    E[A - 1].append(B - 1)
    E[B - 1].append(A - 1)

queue = deque([(0, 0)])
depth = [None] * N
while queue:
    d, q = queue.popleft()
    depth[q] = d

    for e in E[q]:
        if depth[e] is None: queue.append((d + 1, e))

for _ in range(Q):
    C, D = map(int, input().split())
    print('Town' if depth[C - 1] % 2 == depth[D - 1] % 2 else 'Road')
