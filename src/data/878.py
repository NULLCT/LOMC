from collections import deque

n, q = (int(x) for x in input().split())
town = []
root = [[] for i in range(n)]
dis = [-1 for i in range(n)]
dis[0] = 0

for i in range(n - 1):
    a, b = (int(x) for x in input().split())
    root[a - 1].append(b)
    root[b - 1].append(a)
for i in range(q):
    c, d = (int(x) for x in input().split())
    town.append((c, d))
dis = [-1 for i in range(n)]
dis[0] = 0

for i in range(len(root[0])):
    if i == 0:
        que = deque([[root[0][i], 0]])
    else:
        que.appendleft([root[0][i], 0])
while que:
    go, dist = que.pop()
    dis[go - 1] = dist + 1
    for i in root[go - 1]:
        if dis[i - 1] == -1:
            que.appendleft([i, dist + 1])
for c, d in town:
    if (dis[c - 1] - dis[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
