from collections import deque

N, Q = map(int, input().split())
road = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)

query = []
for i in range(Q):
    query.append([int(x) - 1 for x in input().split()])

q = deque([0])
dis = [-1] * N
dis[0] = 0
while q:
    town = q.popleft()
    for i in road[town]:
        if dis[i] == -1:
            dis[i] = dis[town] + 1
            q.append(i)

for i in range(Q):
    if (dis[query[i][0]] - dis[query[i][1]]) % 2 == 0:
        print("Town")
    else:
        print("Road")
