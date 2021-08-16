inputs = input().split()
inputs = list(map(int, inputs))
N = inputs[0]
Q = inputs[1]

roads = [[] for _ in range(N)]
for road_idx in range(N - 1):
    inputs = input().split()
    inputs = list(map(int, inputs))
    roads[inputs[0] - 1].append(inputs[1] - 1)
    roads[inputs[1] - 1].append(inputs[0] - 1)

flags = [False for _ in range(N)]
flags[0] = True
distances = [-1 for _ in range(N)]
distances[0] = 0
queue = [0]
while len(queue) > 0:
    current = queue.pop(0)
    for neighbor in roads[current]:
        if not flags[neighbor]:
            distances[neighbor] = distances[current] + 1
            queue.append(neighbor)
            flags[neighbor] = True

for _ in range(Q):
    inputs = input().split()
    inputs = list(map(int, inputs))
    s = inputs[0] - 1
    g = inputs[1] - 1
    distance = distances[s] + distances[g]
    if distance % 2 == 0:
        print('Town')
    else:
        print('Road')
