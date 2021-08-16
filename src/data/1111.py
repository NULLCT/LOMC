N, Q = map(int, input().split())

V = [[] * N for i in range(0, N)]

for i in range(0, N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    V[A].append([B, A])
    V[B].append([A, B])

import collections

Visited = [-1] * N
Visited[0] = 0

import copy

d = copy.deepcopy(V[0])
q = collections.deque(d)

while q:
    d = q.popleft()
    A = d[0]
    B = d[1]
    if Visited[A] != -1:
        pass
    else:
        Visited[A] = Visited[B] + 1
        for i in range(0, len(V[A])):
            q.append(V[A][i])

for i in range(0, Q):
    C, D = map(int, input().split())
    if (Visited[C - 1] + Visited[D - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
