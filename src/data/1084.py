import sys
from collections import deque


class RootTree(object):
    def __init__(self, v, e, root=0):
        """[summary]

        Args:
            v (int): num of vartex
            e (list): list of edges(1-indexed)
        """
        self.v = v
        self.root = root
        self.parent = [root] * v
        self.depth = [0] * v
        self.children = [set([]) for _ in range(v)]
        self.edge = e

        tempchildren = [[] for _ in range(v)]
        for a, b in e:
            a, b = a - 1, b - 1
            tempchildren[a].append(b)
            tempchildren[b].append(a)

        que = deque([])
        que.append(root)
        frag = [False] * v
        frag[root] = True
        while len(que) > 0:
            q = que.popleft()
            for p in tempchildren[q]:
                if frag[p]: continue
                frag[p] = True
                self.children[q].add(p)
                self.parent[p] = q
                self.depth[p] = self.depth[q] + 1
                que.append(p)

    def bfs(self, v_i):
        que = deque([v_i])
        while (len(que) > 0):
            q = que.popleft()
            yield q
            for c in self.children[q]:
                que.append(c)

    def dfs(self, v_i):
        que = [v_i]
        while (len(que) > 0):
            q = que.pop()
            yield q
            for c in self.children[q]:
                que.append(c)

    def diameter(self):
        _, idx = max([(d, i) for (i, d) in enumerate(self.depth)])
        t = RootTree(self.v, self.edge, root=idx)
        return max(t.depth)

    def eulartour(self):
        que = [self.root]
        frag = [False] * self.v
        while (len(que) > 0):
            q = que.pop()
            yield q
            if frag[q]: continue
            for c in self.children[q]:
                que.append(q)
                que.append(c)
            frag[q] = True

    def buildLCA(self):
        return RootTree.LCA(self)

    class LCA(object):
        class SparseTable(object):
            def __init__(self, lst, operator, idm):
                n = len(lst)
                max_k = n.bit_length() + 1
                table = [[idm] * max_k for _ in range(n)]
                for i in range(n):
                    table[i][0] = lst[i]
                for k in range(1, max_k):
                    for i in range(n + 1 - (1 << k)):
                        table[i][k] = operator(
                            table[i][k - 1], table[i + (1 << (k - 1))][k - 1])

                logtable = [0] * (n + 1)
                for i in range(2, n + 1):
                    logtable[i] = logtable[i >> 1] + 1
                self.table = table
                self.logtable = logtable
                self.operator = operator

            def query(self, l, r):
                """operated value of [l, r)

                Args:
                    l (int): left closed interval
                    r (int): right open interval
                """
                k = self.logtable[r - l]
                return self.operator(self.table[l][k],
                                     self.table[r - (1 << k)][k])

        def __init__(self, roottree):
            eulartour = []
            self.firstappear = [-1] * roottree.v
            for i, v in enumerate(roottree.eulartour()):
                if self.firstappear[v] == -1:
                    self.firstappear[v] = i
                eulartour.append((roottree.depth[v], v))

            self.sparse = RootTree.LCA.SparseTable(eulartour, min,
                                                   (10**18, -1))

        def query(self, v1, v2):
            l, r = self.firstappear[v1], self.firstappear[v2]
            if l > r:
                l, r = r, l
            _, v = self.sparse.query(l, r + 1)
            return v


def readint():
    return int(sys.stdin.readline())


def readints():
    return tuple(map(int, sys.stdin.readline().split()))


def readintslist(n):
    return [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]


def main():
    n, q = readints()
    edges = []
    for _ in range(n - 1):
        a, b = readints()
        edges.append((a, b))

    tree = RootTree(n, edges)
    lca = tree.buildLCA()

    #print(tree.depth)

    for c, d in readintslist(q):
        c, d = c - 1, d - 1
        common = lca.query(c, d)
        dist = tree.depth[c] + tree.depth[d] - 2 * tree.depth[common]

        if dist % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
