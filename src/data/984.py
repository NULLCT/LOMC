from collections import deque

n, q = map(int, input().split())

edges = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)

CNT = [-1] * n
CNT[0] = 0

DQ = deque([0])

while DQ:
    x = DQ.popleft()
    for y in edges[x]:
        if CNT[y] >= 0:
            continue
        CNT[y] = CNT[x] + 1
        DQ.append(y)
# print(CNT)

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (CNT[c] - CNT[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
