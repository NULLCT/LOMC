from collections import deque

n, q = map(int, input().split())
ct = [[] for _ in range(n)]

inz = lambda x: int(x) - 1

for i in range(n - 1):
    a, b = map(inz, input().split())
    ct[a].append(b)
    ct[b].append(a)

dst = [-1] * n
dst[0] = 0
nxt = deque()
nxt.append(0)

while nxt:
    pos = nxt.popleft()
    for i in ct[pos]:
        if dst[i] == -1:
            dst[i] = dst[pos] + 1
            nxt.append(i)

for i in range(q):
    c, d = map(inz, input().split())
    if abs(dst[c] - dst[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
