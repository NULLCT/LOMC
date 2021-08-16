import sys
from collections import deque

N, Q = map(int, input().split())
visited = [False] * (N + 1)
connected = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    connected[a].append(b)
    connected[b].append(a)
distancefromone = [0] * (N + 1)
Que = deque([1])
count = 1
visited[1] = True
while Que:
    for _ in range(len(Que)):
        p = Que.popleft()
        for v in connected[p]:
            if visited[v] == False:
                distancefromone[v] = count
                visited[v] = True
                Que.append(v)
    count += 1
for _ in range(Q):
    c, d = map(int, sys.stdin.readline().split())
    distance = abs(distancefromone[c] - distancefromone[d])
    if distance % 2 == 0:
        print('Town')
    else:
        print('Road')
