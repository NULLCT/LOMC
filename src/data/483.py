import queue

N, Q = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
que = queue.Queue()
dep = [-1] * N
dep[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in G[t]:
        if dep[i] == -1:
            dep[i] = dep[t] + 1
            que.put(i)
for _ in range(Q):
    c, d = map(int, input().split())
    if (dep[c - 1] + dep[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
