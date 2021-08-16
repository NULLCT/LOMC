import queue

N, Q = map(int, input().split())
X = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    X[a - 1].append(b - 1)
    X[b - 1].append(a - 1)

color = [-1] * N
color[0] = 0
q = queue.Queue()
q.put(0)
while not q.empty():
    t = q.get()
    for i in X[t]:
        if color[i] == -1:
            color[i] = color[t] ^ 1
            q.put(i)

for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
