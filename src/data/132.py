import queue

N, Q = map(int, input().split())
A = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    A[a - 1].append(b - 1)
    A[b - 1].append(a - 1)
q = queue.Queue()
dis = [-1] * N
dis[0] = 0
q.put(0)
while not q.empty():
    t = q.get()
    for i in A[t]:
        if dis[i] == -1:
            dis[i] = 1 - dis[t]
            q.put(i)
for _ in range(Q):
    c, d = map(int, input().split())
    if dis[c - 1] == dis[d - 1]:
        print('Town')
    else:
        print('Road')
