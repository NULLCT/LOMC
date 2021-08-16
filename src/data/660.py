import queue

#Data Input
N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
que = queue.Queue()
C = [-1] * N
C[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in G[t]:
        if C[i] == -1:
            C[i] = 1 - C[t]
            que.put(i)

for i in range(Q):
    x, y = map(int, input().split())
    if (C[x - 1] - C[y - 1]) % 2 == 1:
        print('Road')
    else:
        print('Town')
