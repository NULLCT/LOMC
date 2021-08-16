from collections import deque


def bfs():
    cities_to_go = deque()
    cities_to_go.append(0)
    # 0 distance to the start point
    distances[0] = 0

    while len(cities_to_go) > 0:
        city_to_go = cities_to_go.popleft()
        for next_city in routes[city_to_go]:
            if distances[next_city] == -1:
                cities_to_go.append(next_city)
                distances[next_city] = distances[city_to_go] + 1


n, q = map(int, input().split())
routes = [[] for _ in range(n)]
# create routes
for _ in range(n - 1):
    a, b = map(int, input().split())
    routes[a - 1].append(b - 1)
    routes[b - 1].append(a - 1)
# calculate all distances from city 0
distances = [-1] * n
bfs()
# print based on query
for _ in range(q):
    c, d = map(int, input().split())
    if (distances[c - 1] - distances[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
