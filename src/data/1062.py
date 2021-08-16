import sys

sys.setrecursionlimit(10**6)


class Tree:
    class Edge:
        def __init__(self, to, rev):
            self.to = to
            self.rev = rev

    def __init__(self, V):
        self.V = V
        self.G = [[] for _ in range(V)]
        self.p = [0] * V
        self.depth = [0] * V

    def addEdge(self, fm, to):
        self.G[fm].append(self.Edge(to, len(self.G[to])))
        self.G[to].append(self.Edge(fm, len(self.G[fm]) - 1))

    def setRoot(self, root):
        self.root = root
        self.setParent(root, -1, 0)

    def setParent(self, cur, parent, d):
        self.p[cur] = parent
        self.depth[cur] = d
        for e in self.G[cur]:
            if e.to != parent:
                self.setParent(e.to, cur, d + 1)

    def getDepth(self, p):
        return self.depth[p]


n, q = map(int, input().split())
tree = Tree(n)
for i in range(n - 1):
    a, b = map(int, input().split())
    tree.addEdge(a - 1, b - 1)
tree.setRoot(0)
for i in range(q):
    c, d = map(int, input().split())
    depth_diff = abs(tree.getDepth(c - 1) - tree.getDepth(d - 1))
    print("Town" if depth_diff % 2 == 0 else "Road")
