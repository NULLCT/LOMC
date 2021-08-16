from collections import deque


class Node:
    def __init__(self, index):
        self.color = None
        self.nears = []
        self.safe = -1


n, q = map(int, input().split())
nodes = [Node(i) for i in range(n + 1)]
for j in range(n - 1):
    a, b = map(int, input().split())
    nodes[a].nears.append(b)
    nodes[b].nears.append(a)

de = deque()
de.append(nodes[1])
nodes[1].safe = 1
nodes[1].color = "red"
u = 0
while de:
    for k in range(len(de)):
        s = de.popleft()
        nears = s.nears
        for near in nears:
            if nodes[near].safe == -1:
                nodes[near].safe = 1
                de.append(nodes[near])
                if u % 2 == 0:
                    nodes[near].color = "blue"
                else:
                    nodes[near].color = "red"
    u += 1
for m in range(q):
    c, d = map(int, input().split())
    if nodes[c].color == nodes[d].color:
        print("Town")
    else:
        print("Road")
