n, q = map(int, input().split())

node = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    node[a - 1].append(b)
    node[b - 1].append(a)

town = [2] * n
town[0] = 0
node_bool = [True] * n
node_bool[0] = False

from collections import deque

d = deque()
for j in node[0]:
    d.append(j)
    node_bool[j - 1] = False
    town[j - 1] = 1

while d:
    v = d.popleft()
    for j in node[v - 1]:
        if node_bool[j - 1]:
            node_bool[j - 1] = False
            d.append(j)
            if town[v - 1] == 1:
                town[j - 1] = 0
            elif town[v - 1] == 0:
                town[j - 1] = 1

cd = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    if town[cd[i][0] - 1] == town[cd[i][1] - 1]:
        print('Town')
    else:
        print('Road')
