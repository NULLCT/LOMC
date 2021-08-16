def resolve():
    import sys
    sys.setrecursionlimit(2147483647)
    INF = float("inf")
    MOD = 10**9 + 7
    input = sys.stdin.readline

    class LCA:
        """
        construct: O(NlogN)
        query: O(logN)
        """
        def __init__(self, edges, root=0):
            """
            :param list of (list of int) edges:
            :param int root=0:
            """
            self.edges = edges
            self.n = len(edges)  # n=|V|
            self.logn = (self.n - 1).bit_length()  # logn=ceil(log2(n))
            self.depths = [-1] * self.n
            self.parents = [[-1] * self.n for _ in range(self.logn)]
            # construct
            self.__dfs(-1, root, 0)
            self.__doubling()

        def __dfs(self, par, cur, dep):
            self.depths[cur] = dep
            self.parents[0][cur] = par
            for v in self.edges[cur]:
                if self.depths[v] == -1:  # 深さ-1＝訪れていない(rootから連結な部分しか探索しない)
                    self.__dfs(cur, v, dep + 1)

        def __doubling(self):
            for i in range(1, self.logn):
                for v in range(self.n):
                    if self.parents[
                            i - 1][v] == -1:  # 親が存在しないとき。-1を通すとlistの末尾を取得してしまう
                        continue
                    self.parents[i][v] = self.parents[i -
                                                      1][self.parents[i -
                                                                      1][v]]

        def get(self, u, v):  # u,vのLCAを返す
            dd = self.depths[v] - self.depths[u]
            if dd < 0:  # vの方が深いようにする
                u, v = v, u
                dd *= -1
            for i in range(self.logn):
                if dd & (1 << i):
                    v = self.parents[i][v]

            if v == u: return v  # 高さ揃えた時点で一致してたら終わり

            # そうでなければ上から二分探索
            for i in reversed(range(self.logn)):
                pu, pv = self.parents[i][u], self.parents[i][v]
                if pu != pv:
                    u, v = pu, pv
            return self.parents[0][u]

    # input
    n, Q = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        edges[u].append(v)
        edges[v].append(u)
    lca = LCA(edges)
    for _ in range(Q):
        u, v = map(lambda x: int(x) - 1, input().split())
        if (lca.depths[u] + lca.depths[v] -
                2 * lca.depths[lca.get(u, v)]) % 2 == 0:
            print("Town")
        else:
            print("Road")


resolve()
