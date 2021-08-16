class RmQWithSparseTable:
    """
    RmQ特化型クラス sparse_tableを用いている 空間計算量は大きいことに注意
    計算量 構築O(NlogN) クエリO(1)
    https://tookunn.hatenablog.com/entry/2016/07/13/211148 <--基本的にはこの実装
    https://ikatakos.com/pot/programming_algorithm/data_structure/sparse_table
    https://www.topcoder.com/thrive/articles/Range%20Minimum%20Query%20and%20Lowest%20Common%20Ancestor
    """
    def __init__(self, array, is_for_return_index=True):
        N = len(array)
        logN = N.bit_length()
        log_table = [0] * (N + 1)
        for i in range(2, N + 1):
            log_table[i] = log_table[i >> 1] + 1
        sparse_table = [[0] * (N)
                        for i in range(log_table[N] + 1)]  # 参考文献とは順序を変えた
        sparse_table[0] = list(range(N)) if is_for_return_index else array
        if is_for_return_index:
            for k in range(1, logN):
                for i in range(N):
                    if i + (1 << k) > N:
                        break
                    first = sparse_table[k - 1][i]
                    second = sparse_table[k - 1][i + (1 << (k - 1))]
                    sparse_table[k][i] = first if array[first] <\
                        array[second] else second
        else:  # この方針ではindexの保持も値の保持も本質的には同じ
            for k in range(1, logN):
                for i in range(N):
                    if i + (1 << k) > N:
                        break
                    sparse_table[k][i] = min(
                        sparse_table[k - 1][i],
                        sparse_table[k - 1][i + (1 << (k - 1))])
        self.array = array
        self.log_table = log_table
        self.sparse_table = sparse_table
        self.mode = is_for_return_index

    def query(self, l, r):
        """
        array[l:r]の最小を返す 半開区間、0-indexed
        仕組み ざっくり言えば、クエリの区間に応じてアクセスする節の大きさを決める感じ
        stk[l],stk[r-(1<<k)]でそれぞれ1<<k個の区間の最小値が分かるので、
        全体の区間の最小値はそのいずれか 冪等性(A•A==A)を満たすならば、他にも応用可
        """
        d = r - l
        k = self.log_table[d]
        stk = self.sparse_table[k]
        if self.mode:
            return stk[l] if self.array[stk[l]] < self.array[stk[r-(1 << k)]]\
                else stk[r-(1 << k)]
        else:
            return min(stk[l], stk[r - (1 << k)])


class LCA(RmQWithSparseTable):
    def __init__(self, adj):
        self.adj = adj
        self.vs, self.depth, self.id = self.euler_tour(self.adj, start_node=0)
        super().__init__(self.depth, is_for_return_index=True)

    def euler_tour(self, adj: list, start_node: int = 0):
        """
        根からDFSをし、その順に番号を付けていく 蟻本p.294の非再帰版 自作につき壊れに注意
        """
        MAX_V = len(adj)
        vs = [0] * (2 * MAX_V - 1)  # DFSでの訪問順
        depth = [0] * (2 * MAX_V - 1)  # 根からの深さ
        id = [0] * MAX_V  # 各頂点がvsにはじめて登場するインデックス
        k = -1  # 何番目の訪問であるか
        d = -1  # 現時点での深さ
        visited = [False] * MAX_V
        stack = [start_node]
        while stack:
            from_node = stack.pop()
            if from_node >= 0:  # 行き
                visited[from_node] = True
                d += 1  # dやkの扱いを蟻本と変えているのは非再帰だから
                k += 1  # euler_tourを辺の往復で考えると理由が分かりやすい
                id[from_node] = k
                vs[k] = from_node
                depth[k] = d
                for to_node in adj[from_node]:
                    if visited[to_node]:
                        continue
                    stack.append(~from_node)  # これも辺の往復で考えるとよい
                    stack.append(to_node)  # 通常のdfsと仕様が異なるので注意
            else:  # 帰り
                d -= 1
                k += 1
                vs[k] = ~from_node
                depth[k] = d
        return vs, depth, id

    def lca(self, u, v):  # 計算量 O(1)
        return self.vs[super().query(min(self.id[u], self.id[v]),
                                     max(self.id[u], self.id[v]) + 1)]

    def dist(self, u, v):  # 計算量 O(1)
        return self.depth[self.id[u]]+self.depth[self.id[v]]\
            - 2*self.depth[self.id[self.lca(u, v)]]


# 以上LCA用コード


def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)

    lca = LCA(adj)

    for q in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        dist = lca.dist(c, d)
        if dist % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
