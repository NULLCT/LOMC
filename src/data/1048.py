from collections import deque

d = deque()
n, q = map(int, input().split())
link = [[] for _ in range(n)]
distant = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    link[a - 1].append(b - 1)
    link[b - 1].append(a - 1)
d.append((0, 0))
while d:
    now, ct = d.popleft()
    if distant[now] or (ct != 0 and now == 0):
        continue
    distant[now] = ct
    for nxt in link[now]:
        d.append((nxt, ct + 1))
for _ in range(q):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if abs(distant[a] - distant[b]) % 2 == 0:
        print("Town")
    else:
        print("Road")
