def LI():
    return list(map(int, input().split()))


n, q = LI()
edges = [[] * n for _ in range(n)]

for _ in range(n - 1):
    a, b = LI()
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

Q = [LI() for _ in range(q)]

from collections import deque

val = [-1] * n
q = deque()
q.append(0)
val[0] = 0
while q:
    p = q.popleft()
    now = val[p]
    nxt = 1 - now
    for c in edges[p]:
        if val[c] != -1:
            continue
        val[c] = nxt
        q.append(c)

for c, d in Q:
    c -= 1
    d -= 1
    if val[c] == val[d]:
        print("Town")
    else:
        print("Road")
