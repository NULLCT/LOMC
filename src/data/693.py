from collections import deque
import copy

n, q = map(int, input().split())
road = []
dist2 = []
for i in range(n):
    road.append([])
    dist2.append(-1)
for i in range(n - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)
Q = deque()
Q.append(0)
while len(Q) > 0:
    i = Q.popleft()
    for j in road[i]:
        if dist2[j] == -1:
            dist2[j] = dist2[i] + 1
            Q.append(j)
for i, d in enumerate(dist2):
    if d % 2 == 0:
        dist2[i] = 1
    else:
        dist2[i] = 2
for i in range(q):
    c, d = map(int, input().split())
    if dist2[c - 1] == dist2[d - 1]:
        print('Town')
    else:
        print('Road')
