import sys

sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())
links = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

D = [0] * N
import queue

que = queue.deque()
que.append((0, -1))
while que:
    x, par = que.pop()
    for nx in links[x]:
        if nx == par:
            continue

        D[nx] = D[x] + 1
        que.append((nx, x))

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if D[c] % 2 == D[d] % 2:
        print("Town")
    else:
        print("Road")
