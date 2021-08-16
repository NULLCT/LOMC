from queue import Queue

n, q = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

que = Queue()
col = [-1] * n
col[0] = 0
que.put(0)

while not que.empty():
    t = que.get()
    for i in g[t]:
        if col[i] == -1:
            col[i] = 1 - col[t]
            que.put(i)

for i in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if col[c] == col[d]:
        print("Town")
    else:
        print("Road")
