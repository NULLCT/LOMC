import queue

n, q = map(int, input().split())
eo = [0 for _ in range(n + 1)]
ab = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)
qq = queue.Queue()
qq.put((1, 1))
while not qq.empty():
    s, p = qq.get()
    eo[s] = p
    for t in ab[s]:
        if eo[t] == 0:
            qq.put((t, -p))
for i in range(q):
    c, d = map(int, input().split())
    if eo[c] == eo[d]:
        print("Town")
    else:
        print("Road")
