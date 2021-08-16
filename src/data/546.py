from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = False
        self.color = "r"


n, q = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(n - 1)]

nodes = []
for i in range(n + 1):
    nodes.append(Node(i))

for j in range(n - 1):
    edge_start, edge_end = links[j]
    nodes[edge_start].nears.append(edge_end)
    nodes[edge_end].nears.append(edge_start)

queue = deque()
queue.append(nodes[1])

while queue:
    node = queue.popleft()
    nears = node.nears

    for near in nears:
        if nodes[near].sign == False:
            queue.append(nodes[near])
            nodes[near].sign = True
            if node.color == "r":
                nodes[near].color = "b"
            else:
                nodes[near].color = "r"

for k in range(q):
    c, d = map(int, input().split())

    if nodes[c].color == nodes[d].color:
        print("Town")
    else:
        print("Road")
