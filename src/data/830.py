from collections import deque

n, q = map(int, input().split())
path = [[] for i in range(n)]
query = []
for i in range(n - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
for i in range(q):
    c, d = map(int, input().split())
    query.append([c, d])

que = deque()
que.append(0)
city = [-1] * n
city[0] = 0
while len(que) > 0:
    temp = que.pop()
    for i in path[temp]:
        if city[i] != -1:
            continue
        else:
            city[i] = 1 - city[temp]
            que.append(i)

for i in range(q):
    if city[query[i][0] - 1] == city[query[i][1] - 1]:
        print("Town")
    else:
        print("Road")
