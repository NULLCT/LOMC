from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.dis = 0
        self.visited = 0


N, Q = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N - 1)]
queries = [list(map(int, input().split())) for _ in range(Q)]

nodes = []
for i in range(N + 1):
    nodes.append(Node(i))

for map in maps:
    a, b = map
    nodes[a].nears.append(b)
    nodes[b].nears.append(a)

queue = deque()
queue.append(nodes[1])
nodes[1].visited = 1

while queue:
    node = queue.popleft()
    nears = node.nears
    for near in nears:
        if nodes[near].visited == 0:
            queue.append(nodes[near])
            nodes[near].visited = 1
            nodes[near].dis = node.dis + 1

for query in queries:
    _c, _d = query
    c = nodes[_c].dis
    d = nodes[_d].dis
    if (c - d) % 2 == 0:
        print("Town")
    else:
        print("Road")
