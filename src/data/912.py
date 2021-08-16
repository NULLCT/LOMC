from collections import deque

n, q = map(int, input().split())
R = [list(map(int, input().split())) for _ in range(n - 1)]
Q = [list(map(int, input().split())) for _ in range(q)]
near = [[] for _ in range(n + 1)]
for r in R:
    near[r[0]].append(r[1])
    near[r[1]].append(r[0])

queue = deque()
city = [-1 for _ in range(n + 1)]
city[1] = 0
queue.append(1)

while len(queue) > 0:
    i = queue.popleft()
    for c in near[i]:
        if city[c] != -1:
            continue
        else:
            city[c] = 1 - city[i]
            queue.append(c)

for query in Q:
    if city[query[0]] == city[query[1]]:
        print("Town")
    else:
        print("Road")
