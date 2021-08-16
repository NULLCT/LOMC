import queue

num = [int(s) for s in input().split()]

N = num[0]
Q = num[1]

route = [[] for i in range(N)]

for i in range(N - 1):
    temp = [int(s) for s in input().split()]
    route[temp[0] - 1].append(temp[1] - 1)
    route[temp[1] - 1].append(temp[0] - 1)

que = queue.Queue()

color = [-1] * N

color[0] = 0

que.put(0)

while not que.empty():
    t = que.get()
    for i in route[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)

for i in range(Q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print("Town")
    else:
        print("Road")
