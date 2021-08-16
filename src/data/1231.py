# https://raw.githubusercontent.com/cheran-senthil/PyRival/master/pyrival/data_structures/RangeQuery.py
class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append(
                [func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        assert start < stop
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start],
                         self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]


class LCA:
    def __init__(self, graph, root):
        # O(N * log(N))
        N = len(graph)
        self.graph = graph
        self.root = root

        self.parent = [-1] * N
        self.depth = [-1] * N
        self.eulerTour = []  # length is 2 * (N - 1) + 1
        self.timeIn = [-1] * N  # timeIn[node] == eulerTour.index(node)
        self.timeOut = [-1] * N  # timeOut[node] == eulerTour.rindex(node)

        t = 0
        stack = [root]
        self.depth[root] = 0
        self.parent[root] = -1
        while stack:
            node = stack.pop()
            self.eulerTour.append(node)
            if self.timeIn[node] == -1:
                self.timeIn[node] = t
                for child in reversed(graph[node]):
                    if self.timeIn[child] == -1:
                        self.depth[child] = self.depth[node] + 1
                        self.parent[child] = node
                        stack.append(node)
                        stack.append(child)
            self.timeOut[node] = t
            t += 1
            # assert len(self.eulerTour) == t

        self.rmq = RangeQuery(self.timeIn[node] for node in self.eulerTour)

    def lca(self, u, v):
        # O(1)
        # Might also want to prevent inlining, see https://foss.heptapod.net/pypy/pypy/-/issues/1822#note_41573
        # for _ in range(1): pass
        a = self.timeIn[u]
        b = self.timeIn[v]
        if a > b:
            a, b = b, a
        return self.eulerTour[self.rmq.query(a, b + 1)]

    def isAncestor(self, u, v):
        # O(1)
        return self.timeIn[u] <= self.timeIn[v] and self.timeOut[
            v] <= self.timeOut[u]

    def getDist(self, u, v):
        # O(1)
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

    def isPath(self, a, b, c):
        # O(1)
        # Returns whether b is on the path between a and c
        return self.getDist(a, b) + self.getDist(b, c) == self.getDist(a, c)

    def getPath(self, u, v):
        # O(N)
        anc = self.lca(u, v)
        uPath = [u]
        while uPath[-1] != anc:
            uPath.append(self.parent[uPath[-1]])
        vPath = [v]
        while vPath[-1] != anc:
            vPath.append(self.parent[vPath[-1]])
        assert uPath[-1] == vPath[-1]
        uPath.pop()
        return uPath + vPath[::-1]

    def getSubTreeCount(self, u, p=None):
        # O(1)
        # Get the size of the subtree where u is the root with p as the parent
        # Note: p == None here means optional arg
        if p is None or p == self.parent[u]:
            numEdges = (self.timeOut[u] - self.timeIn[u]) // 2
            return numEdges + 1
        return len(self.graph) - self.getSubTreeCount(p)


N, Q = [int(x) for x in input().split()]
AB = [[int(x) - 1 for x in input().split()] for i in range(N - 1)]
CD = [[int(x) - 1 for x in input().split()] for i in range(Q)]

graph = [[] for i in range(N)]
for u, v in AB:
    graph[u].append(v)
    graph[v].append(u)

rootedTree = LCA(graph, 0)

for u, v in CD:
    d = rootedTree.getDist(u, v)
    if d % 2 == 1:
        print("Road")
    else:
        print("Town")
