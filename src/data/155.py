from collections import deque

n, q = map(int, input().split())
ab = []
neighbors = [[] for i in range(n)]
for i in range(n - 1):
    ab.append(list(map(int, input().split())))
for i in range(n - 1):
    neighbors[ab[i][0] - 1].append(ab[i][1] - 1)
    neighbors[ab[i][1] - 1].append(ab[i][0] - 1)
cd = []
for i in range(q):
    cd.append(list(map(int, input().split())))

colors = [None] * n
que = deque()

que.append(0)
colors[0] = "blue"

while que:
    item = que.pop()
    for neighbor in neighbors[item]:
        if not colors[neighbor]:
            if colors[item] == "blue":
                colors[neighbor] = "red"
            if colors[item] == "red":
                colors[neighbor] = "blue"
            que.append(neighbor)
            neighbors[neighbor].remove(item)

for i in range(q):
    if colors[cd[i][0] - 1] == colors[cd[i][1] - 1]:
        print("Town")
    else:
        print("Road")
