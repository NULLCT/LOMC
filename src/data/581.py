import sys
import queue

from operator import itemgetter

sys.setrecursionlimit(1000000)


def input():
    return sys.stdin.readline().rstrip()


N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]

path = [[] for _ in range(N + 1)]
for a, b in ab:
    path[a].append(b)
    path[b].append(a)

# dit[i] は 1からiまでの距離
dist = [None] * (N + 1)
dist[1] = 0

q = queue.Queue()
q.put(1)
while not q.empty():
    root = q.get()
    for chil in path[root]:
        if dist[chil] is None:
            dist[chil] = dist[root] + 1
            q.put(chil)

for i in range(Q):
    c, d = list(map(int, input().split()))
    print(["Town", "Road"][(dist[c] + dist[d]) % 2])
