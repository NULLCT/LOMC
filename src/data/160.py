import queue

que = queue.Queue()
n, q = map(int, input().split())
a = []
b = []
c = []
d = []

for i in range(n - 1):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
for i in range(q):
    x, y = map(int, input().split())
    c.append(x)
    d.append(y)

f = [-1 for i in range(n)]
p = [[] for i in range(n)]

for i in range(n - 1):
    p[a[i] - 1].append(b[i] - 1)
    p[b[i] - 1].append(a[i] - 1)
f[0] = 0
que.put(0)

while not que.empty():
    po = que.get()
    for i in p[po]:
        if f[i] == -1:
            que.put(i)
            f[i] = f[po] + 1

for i in range(q):
    if f[c[i] - 1] % 2 == f[d[i] - 1] % 2:
        print('Town')
    else:
        print('Road')
