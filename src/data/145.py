def PaintColor(color):
    if color == "r":
        return "b"
    else:
        return "r"


import queue as q

N, Q = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(N - 1):
    ai, bi = map(int, input().split())
    G[ai - 1].append(bi - 1)
    G[bi - 1].append(ai - 1)

q = q.Queue()
color = ["w"] * N

q.put(0)
now_color = "r"
color[0] = now_color

while q.qsize():
    v = q.get()
    now_color = PaintColor(color[v])
    for vv in G[v]:
        if color[vv] == "w":
            color[vv] = now_color
            q.put(vv)
"""
for i in range(N):
    print("Town" + str(i+1) + ": " + color[i])
"""

Query = []
for _ in range(Q):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    Query.append([ci, di])

for i in range(Q):
    if color[Query[i][0]] == color[Query[i][1]]:
        print("Town")
    else:
        print("Road")
