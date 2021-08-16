from collections import deque

n, q = map(int, input().split())
con = [set() for i in range(n + 1)]

for i in range(n - 1):
    _a, _b = map(int, input().split())
    con[_a].add(_b)
    con[_b].add(_a)

dq = deque()
dist = [0 for i in range(n + 1)]
for i in con[i]:
    dq.append(i)
    dist[i] = 1

while len(dq) != 0:
    k = dq.popleft()
    for i in con[k]:
        if dist[i] == 0 or dist[i] > dist[k] + 1:
            dq.append(i)
            dist[i] = dist[k] + 1

for i in range(q):
    _c, _d = map(int, input().split())
    if (dist[_c] + dist[_d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
