from collections import deque

n, z = map(int,
           input().split())
p, e, q = [[] for _ in range(n)], [0] * n, deque([0])
e[0] = 1
for i in range(n - 1):
    a, b = map(int,
               input().split())
    p[a - 1].append(b - 1)
    p[b - 1].append(a - 1)
while len(q):
    m = q.popleft()
    for i in p[m]:
        if e[i] == 0:
            e[i] = e[m] + 1
            q.append(i)
for i in range(z):
    c, d = map(int,
               input().split())
    print("Road") if (e[c - 1] - e[d - 1]) % 2 else print("Town")
