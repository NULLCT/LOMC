N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    G[A].append(B)
    G[B].append(A)
Dist = [-1] * N
Dist[0] = 0
Queue = [0]
while Queue:
    V = Queue.pop()
    for v in G[V]:
        if Dist[v] != -1: continue
        Queue.append(v)
        Dist[v] = Dist[V] + 1
for _ in range(Q):
    A, B = map(lambda x: int(x) - 1, input().split())
    print('Road' if (Dist[A] + Dist[B]) % 2 else 'Town')