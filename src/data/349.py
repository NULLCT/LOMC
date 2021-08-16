import queue

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
l = queue.Queue()
eo = [-1] * n
eo[0] = 0
l.put(0)
while l.empty() == False:
    t = l.get()
    for i in g[t]:
        if eo[i] == -1:
            eo[i] = 1 - eo[t]
            l.put(i)
for i in range(q):
    a, b = map(int, input().split())
    if eo[a - 1] == eo[b - 1]:
        print("Town")
    else:
        print("Road")
