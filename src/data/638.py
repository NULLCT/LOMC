import queue

n, q = list(map(int, input().split()))
d = {}
e = [-1] * n
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    if a - 1 not in d: d[a - 1] = []
    if b - 1 not in d: d[b - 1] = []
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)
e[0] = 1
que = queue.Queue()
que.put(0)
while not que.empty():
    t = que.get()
    for i in d[t]:
        if e[i] == -1:
            que.put(i)
            e[i] = 1 - e[t]
for j in range(q):
    a, b = list(map(int, input().split()))
    print("Road" if e[a - 1] - e[b - 1] else "Town")
