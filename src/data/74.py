n, q = (int(x) for x in input().split())
orders = [0 for _ in range(n)]
orders[0] = 1
path = [[] for _ in range(n)]
#print(path)
for i in range(n - 1):
    a, b = (int(x) for x in input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)

from collections import deque

d = deque()
d.append(0)
orders[0] = 1
while d:
    tmp = d.popleft()
    for i in path[tmp]:
        if orders[i] != 0:
            continue
        d.append(i)
        orders[i] = orders[tmp] + 1

ans = []
for i in range(q):
    c, d = (int(x) for x in input().split())
    if orders[c - 1] == orders[d - 1]:
        if (c - 1) in path[d - 1]:
            ans.append("Road")
            continue
    tmp = orders[c - 1] - orders[d - 1]
    if tmp % 2 == 0:
        #print("Town")
        ans.append("Town")
    elif tmp % 2 != 0:
        #print("Road")
        ans.append("Road")
for i in ans:
    print(i)
