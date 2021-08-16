from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


class Tree(object):
    """
    隣接リストによる無向グラフ
    頂点は1-indexed
    """
    def __init__(self):
        self.tree = defaultdict(list)

    def __len__(self):
        """ 頂点数 """
        return len(self.tree)

    def add_edge(self, src, dst, weight=1):
        self.tree[src].append((dst, weight))
        self.tree[dst].append((src, weight))

    def get_nodes(self):
        return self.tree.keys()

    def diameter(self):
        """ 木の直径を求める """
        def dfs(idx, par):
            ret = [0, idx]
            for e, w in self.tree[idx]:
                if e == par:
                    continue
                cost = dfs(e, idx)
                cost[0] += w
                ret = max(ret, cost)
            return ret

        p = dfs(1, -1)
        q = dfs(p[1], -1)
        return q[0]


def main():
    N, Q = map(int, input().split())
    G = Tree()

    for _ in range(N - 1):
        a, b = map(int, input().split())
        G.add_edge(a, b)

    used = set([1])
    P = [0] * N

    def dfs(node, p):
        used.add(node)
        P[node - 1] = p
        for nxt, w in G.tree[node]:
            if nxt not in used:
                dfs(nxt, -p)

    dfs(1, 1)

    for i in range(Q):
        c, d = map(int, input().split())
        print('Town' if P[c - 1] == P[d - 1] else 'Road')


if __name__ == '__main__':
    main()
