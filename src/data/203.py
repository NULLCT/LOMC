N, Q = map(int, input().split())
connections = [[] for _ in range(N)]
# print(len(connections))
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    connections[a].append(b)
    connections[b].append(a)
# print(connections)
roads = [10**5 for _ in range(N)]
roads[0] = 0
dist = 1
towns = connections[0]
while len(towns) > 0:
    nxt = list()
    # print(towns)
    for i in towns:
        if dist < roads[i]:
            nxt.append(i)
        roads[i] = min(roads[i], dist)
    # print("nxt", nxt)
    towns = list()
    for i in nxt:
        towns.extend(connections[i])
    dist += 1
# print(roads)
for j in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    print("Town" if (roads[c] + roads[d]) % 2 == 0 else "Road")
