from collections import deque

n, q = map(int, input().split())
E = [[] for _ in range(n)]
GK = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)
queue = deque()
queue.append(0)
seen = [False] * n
while queue:
    temp = queue.popleft()
    seen[temp] = True
    for e in E[temp]:
        if not seen[e]:
            seen[e] = True
            queue.append(e)
            GK[e] = GK[temp] + 1

for _ in range(q):
    c, d = map(int, input().split())
    if (GK[d - 1] - GK[c - 1]) % 2 == 1:
        print("Road")
    else:
        print("Town")
