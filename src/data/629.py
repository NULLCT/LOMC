def d_collision():
    import sys
    sys.setrecursionlimit(10**7)

    class LowestCommonAncestor(object):
        """木の最近共通祖先を求める"""
        def __init__(self, tree):
            """入力は木を二次元リストで表現したものであることを前提としている"""
            self.n = len(tree)
            self.tree = tree
            # parent[j][k]: 頂点 j から根に向かって 2**k 回進んで到達する頂点
            self.parent = [[] for _ in range(self.n)]
            # depth[j]: 根 (頂点 0) に対する頂点 j の深さ
            self.depth = [None] * self.n
            self.stack = []
            self._make_parent_table(0)

        def _make_parent_table(self, vertex):
            """parent と depth に値を格納"""
            recursion_time = len(self.stack)
            self.depth[vertex] = recursion_time

            # 親を (存在する限り) 2**k 回辿る
            k = 0
            while 2**k <= recursion_time:
                self.parent[vertex].append(self.stack[recursion_time - 2**k])
                k += 1

            self.stack.append(vertex)

            for next_vertex in self.tree[vertex]:
                if self.depth[next_vertex] is not None:
                    continue
                self._make_parent_table(next_vertex)
            self.stack.pop()

        def depth_from_root(self, v):
            return self.depth[v]

        def get_lca(self, u, v):
            """頂点 u, v の LCA を求める"""
            if self.depth[u] > self.depth[v]:  # より深い頂点を v とする
                u, v = v, u

            depth_add = self.depth[u] + self.depth[v]
            depth_diff = self.depth[v] - self.depth[u]

            # u と v が同じ深さになるまで v (深い方) を根に向かって登らせる
            while depth_diff > 0:
                k = 1
                while 2**k < depth_diff:
                    k += 1
                k -= 1

                v = self.parent[v][k]
                depth_diff -= 2**k

            # u と v が同じ頂点を指さないギリギリまで u, v を根に向かって登らせる
            # そこから 1 つ登った頂点は u, v の LCA である
            while u != v:
                k = 1
                length = len(self.parent[u])
                # 登ることができ，親が同じでない
                while length > k and self.parent[u][k] != self.parent[v][k]:
                    k += 1
                k -= 1
                u = self.parent[u][k]
                v = self.parent[v][k]
            return u

    N, Q = [int(_) for _ in input().split()]
    Roads = [[] for _ in range(N)]
    for _ in range(N - 1):
        x, y = [int(i) - 1 for i in sys.stdin.readline().split()]
        Roads[x].append(y)
        Roads[y].append(x)

    lowest_common_ancestor = LowestCommonAncestor(Roads)
    lca = lowest_common_ancestor.get_lca
    d = lowest_common_ancestor.depth_from_root
    ans = []
    add = ans.append

    for _ in range(Q):
        a, b = [int(i) - 1 for i in sys.stdin.readline().split()]
        l = lca(a, b)
        dist = d(a) + d(b) - 2 * d(l) + 1
        add('Road' if dist % 2 == 0 else 'Town')
    return '\n'.join(map(str, ans))


print(d_collision())
