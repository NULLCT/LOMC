#D

from collections import deque

N, Q = map(int, input().split())

AB = [list(map(int, input().split())) for l in range(N - 1)]

CD = [list(map(int, input().split())) for l in range(Q)]

edges = [[] for _ in range(N + 1)]
for a, b in AB:
    edges[a].append(b)
    edges[b].append(a)  #根がはっきりしている場合は不要

done = [0] * (N + 1)

dep = [0] * (N + 1)

q = deque()
q.append([1, 0])
# キューが空になるまで繰り返す
while len(q) > 0:
    # キューの末（右端）からnodeを取り出す
    node = q.pop()
    if node is not None:
        n = node[0]
        c = node[1]
        if done[n] == 0:
            done[n] = 1
            dep[n] = c
            for e in edges[n]:
                q.append([e, c + 1])

for cd in CD:
    c = cd[0]
    d = cd[1]
    if abs(dep[c] - dep[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
