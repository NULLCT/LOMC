import queue

n, q = map(int, input().split())

G = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()

C = [0] * n
C[0] = 1

que.put(0)

while not que.empty():
    t = que.get()
    for i in G[t]:
        if C[i] == 0:
            C[i] = -C[t]
            que.put(i)

for i in range(q):
    a, b = map(int, input().split())
    print("Town" if C[a - 1] * C[b - 1] == 1 else "Road")
