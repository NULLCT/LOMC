from collections import deque

n, q = map(int, input().split())
A = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

D = [0] * (n + 1)
found = deque()
found.append(1)
vit = [0] * (n + 1)
while (found):
    c = found.popleft()
    if vit[c] == 1:
        continue
    vit[c] = 1
    for x in A[c]:
        if vit[x] == 0:
            found.append(x)
            D[x] = 1 - D[c]

for i in range(q):
    a, b = map(int, input().split())
    if D[a] == D[b]:
        print("Town")
    else:
        print("Road")
