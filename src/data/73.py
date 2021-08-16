n, q = map(int, input().split())
ab = [input() for i in range(n - 1)]
que = [input() for i in range(q)]
to = [[] for i in range(n)]
for i in range(len(ab)):
    a, b = map(int, ab[i].split())
    to[a - 1].append(b - 1)
    to[b - 1].append(a - 1)
for i in range(len(que)):
    c, d = map(int, que[i].split())
    que[i] = [c - 1, d - 1]

pari = [0 for i in range(n)]

import queue

qu = queue.Queue()
qu.put(0)
pari[0] = 1
while not qu.empty():
    t = qu.get()
    for i in to[t]:
        if pari[i] != 0:
            continue
        pari[i] = pari[t] % 2 + 1
        qu.put(i)

for i in que:
    if (pari[i[0]] - pari[i[1]]) % 2:
        print("Road")
    else:
        print("Town")
