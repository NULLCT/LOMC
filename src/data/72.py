import heapq

N, Q = map(int, input().split())
road = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)

distance = [0] * N
que = [(0, 0)]
heapq.heapify(que)

arrived = {}
while que:
    now = heapq.heappop(que)
    distance[now[1]] = now[0]
    arrived[now[1]] = 1
    for town in road[now[1]]:
        if town not in arrived:
            heapq.heappush(que, (now[0] + 1, town))

for _ in range(Q):
    c, d = map(int, input().split())
    if (distance[c - 1] - distance[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
