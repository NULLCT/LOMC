import queue
from collections import defaultdict as dd

N, Q = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N - 1)]
cd = [map(int, input().split()) for _ in range(Q)]

tree = dd(set)
eo = [0] * N

for a, b in ab:
    tree[a - 1].add(b - 1)
    tree[b - 1].add(a - 1)

# DFS
q = queue.Queue()
q.put(0)
eo[0] = 1
while not q.empty():
    now = q.get()
    for i, nxt in enumerate(tree[now]):
        if eo[nxt] == 0:
            q.put(nxt)
            eo[nxt] = (eo[now]) % 2 + 1

for c, d in cd:
    if (eo[c - 1] + eo[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
