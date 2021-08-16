from collections import deque


class Node:
    def __init__(self):
        self.color = None
        self.paths = []


n, q = map(int, input().split())
g = [Node() for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].paths.append(b)
    g[b].paths.append(a)

queue = deque()
g[0].color = 1
queue.appendleft(g[0])
while queue:
    node = queue.pop()
    for to_node in node.paths:
        if g[to_node].color is None:
            g[to_node].color = 1 if node.color == 0 else 0
            queue.appendleft(g[to_node])

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if g[c].color == g[d].color:
        print('Town')
    else:
        print('Road')
