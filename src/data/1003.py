from collections import deque

N, Q = map(int, input().split())
chi = [[] for _ in [0] * N]
for _ in [0] * (N - 1):
    a, b = map(int, input().split())
    if b > a: a, b = b, a
    chi[b - 1].append(a)
    chi[a - 1].append(b)
inf = 10**10
d = [inf] * N
q = deque()
q.append(1)
d[0] = 0
while q:
    p = q.popleft()
    for np in chi[p - 1]:
        if d[p - 1] < d[np - 1]:
            d[np - 1] = d[p - 1] + 1
            q.append(np)
for _ in [0] * Q:
    ci, di = map(int, input().split())
    print(['Road', 'Town'][(d[ci - 1] - d[di - 1]) % 2 == 0])
