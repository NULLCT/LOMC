from collections import deque

n, q = map(int, input().split())

w = [[] for i in range(n + 1)]
r = [-1 for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    w[a].append(b)
    w[b].append(a)
for i in range(1, n + 1):
    if len(w[i]) == 1:
        s = i
        break
r[s] = 0
d = deque()
d.append(s)

while d:
    t0 = d.popleft()

    r0 = r[t0] + 1
    for t in w[t0]:
        if r[t] == -1:
            d.append(t)
            r[t] = r0
for i in range(q):
    a, b = map(int, input().split())
    if (r[a] - r[b]) % 2 == 0:
        print("Town")
    else:
        print("Road")
