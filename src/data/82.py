# node n
# edge n-1
# ->tree

n, query = map(int, input().split())

g = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

oe = [-1 for i in range(n + 1)]
check = [0 for i in range(n + 1)]

from collections import deque

q = deque()
q.append(1)

oe[1] = 0

while q:
    now = q.popleft()
    for i in g[now]:
        if (check[i] == 1):
            continue
        q.append(i)
        oe[i] = (oe[now] + 1) % 2
        check[i] = 1

judge = ["Town", "Road"]

for i in range(query):
    c, d = map(int, input().split())
    print(judge[oe[c] ^ oe[d]])
