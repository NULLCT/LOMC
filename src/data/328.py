from collections import deque

n, q = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

li = [0] * n
li[0] = 1
to = deque([0])

lis = [0] * n

while len(to):
    v = to.pop()
    for i in g[v]:
        if li[i]: continue
        li[i] = 1
        lis[i] ^= lis[v] ^ 1
        to.append(i)

ans = []
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if lis[c] == lis[d]: ans.append("Town")
    else: ans.append("Road")

[print(i) for i in ans]
