import sys
import logging
from typing import List, Tuple


def convert_to_tree(undirected_graph: List[List[int]],
                    root: int) -> Tuple[List[List[int]], List[int]]:
    n = len(undirected_graph)

    depths = [-1] * n
    depths[root] = 0

    neighbors_directed: List[List[int]] = [[] for _ in range(n)]
    stack = [root]
    while stack:
        si = stack.pop()

        for adj in undirected_graph[si]:
            if depths[adj] != -1:
                continue
            stack.append(adj)
            depths[adj] = depths[si] + 1
            neighbors_directed[si].append(adj)

    return neighbors_directed, depths


class LowestCommonAncestor:
    """
    ancestors[i][j] = ノードjの2**i個上の祖先

    前処理: O(V log V)
    クエリ: O(log V)

    https://algo-logic.info/lca/

    Verified by
    - https://atcoder.jp/contests/abc014/tasks/abc014_4
    """
    def __init__(self, tree: List[List[int]], depths: List[int], root: int):
        self.n_nodes = len(tree)
        self.depths = depths
        self.root = root

        depth_max = max(self.depths)
        self.h = 1
        while (1 << self.h) < depth_max:
            self.h += 1

        ancestors = [[-1] * self.n_nodes for _ in range(self.h)]

        for i, neighbors in enumerate(tree):
            for j in neighbors:
                ancestors[0][j] = i

        for k in range(self.h - 1):
            for j in range(self.n_nodes):
                if ancestors[k][j] >= 0:
                    ancestors[k + 1][j] = ancestors[k][ancestors[k][j]]
                else:
                    ancestors[k + 1][j] = -1

        self.ancestors = ancestors

    def query(self, u, v) -> int:
        if self.depths[u] < self.depths[v]:
            u, v = v, u

        for k in range(self.h):
            if ((self.depths[u] - self.depths[v]) >> k) & 1:
                u = self.ancestors[k][u]

        if u == v:
            lca = u
        else:
            for k in reversed(range(self.h)):
                if self.ancestors[k][u] != self.ancestors[k][v]:
                    u = self.ancestors[k][u]
                    v = self.ancestors[k][v]
            lca = self.ancestors[0][u]

        return lca


def main():
    n, n_queries = map(int, input().split())
    undirected_tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        undirected_tree[ai].append(bi)
        undirected_tree[bi].append(ai)

    root = 0
    tree, depths = convert_to_tree(undirected_tree, root)

    lca = LowestCommonAncestor(tree, depths, root)

    for _ in range(n_queries):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1
        lca_i = lca.query(ci, di)
        ans = depths[ci] + depths[di] - 2 * depths[lca_i]
        if ans % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    loglevel = "DEBUG" if "--debug" in sys.argv else "WARNING"
    numeric_level = getattr(logging, loglevel, None)
    log_format = "%(levelname)s (%(asctime)s.%(msecs)d): %(message)s"
    logging.basicConfig(level=numeric_level,
                        format=log_format,
                        datefmt="%I:%M:%S")

    main()
