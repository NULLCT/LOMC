class Inputs():
    def inInt():  # 入力行（数値1つ）を整数型にして返す
        return int(input())

    def inInts():  # 入力行をスペース区切りで整数型のリスト化して返す
        return [int(n) for n in input().split()]

    def inIntN(n):  # n行1整数の入力から整数型のリストを作成して返す
        return [int(input()) for _ in range(n)]

    def inIntsN(n):  # n行の入力をスペース区切りで整数型の2次元リストにして返す
        return [list(map(int, input().split())) for _ in range(n)]

    def inChars():  # 入力した文字列を1文字ずつに分解してリスト化して返す
        return list(input())

    def inCharsN(n):  # n行の文字列入力を1文字ずつに分解して2次元リストにして返す
        return [list(input()) for _ in range(n)]

    def inStr():  # 入力行を文字列として格納して返す
        return input()

    def inStrs():  # 入力行をスペース区切りでリスト化して返す
        return input().split()

    def inStrsN(n):  # n行の入力をスペース区切りで文字列型の2次元リストにして返す
        return [input().split() for _ in range(n)]

    def getInitListDim1(val, n):  # 長さnのリストをvalで初期化して返す
        return [val] * (n)

    def getInitListDim2(val, n, m):  # n * mの2次元リストをvalで初期化して返す
        return [[val for _ in range(m)] for _ in range(n)]

    def getInitListDim3(val, n, m, k):  # n * m * kの3次元リストをvalで初期化して返す
        return [[[val for _ in range(k)] for _ in range(m)] for _ in range(n)]


class Outputs():
    def outputs_yes_no(bool):  # AtCoder用のYes/Noの出力用関数
        print('Yes') if bool else print('No')


class UFT:
    def __init__(self, n):
        self.uft = [-1] * (n + 1)

    def find(self, x):
        if self.uft[x] < 0:
            return x
        else:
            self.uft[x] = self.find(self.uft[x])  # 経路圧縮
            return self.uft[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            pass
        else:
            if self.uft[x] > self.uft[y]:
                x, y = y, x
            self.uft[x] += self.uft[y]
            self.uft[y] = x
        return self.uft

    def size(self, x):
        return -self.uft[self.find(x)]


class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.ele = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.ele[i] += x
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.ele[i]
        return self.sum(j) - self.sum(i)


class SegmentTree:
    pass


class Graph:
    INF = 10**9

    def __init__(self, n: int, e: list):
        self.num_nodes = n
        self.num_edges = len(e)
        self.edges = [[] for _ in range(n)]
        for t in e:
            self.edges[t[0] - 1].append(t[1] - 1)
            self.edges[t[1] - 1].append(t[0] - 1)

    def dijkstra(self, s):
        from heapq import heappush, heappop
        dist = [self.INF] * self.num_nodes
        hq = [(0, s)]
        dist[s] = 0
        seen = [False] * self.num_nodes
        while hq:
            v = heappop(hq)[1]
            seen[v] = True
            for to in self.edges[v]:
                if seen[to] is False and dist[v] + 1 < dist[to]:
                    dist[to] = dist[v] + 1
                    heappush(hq, (dist[to], to))
        return dist


class GraphCustomized(Graph):  # 3-coloring @ ABC199D
    import sys
    sys.setrecursionlimit(10**6)

    def __init__(self, n: int, e: list):
        super(GraphCustomized, self).__init__(n, e)
        self.num_components = 0
        self.nodes_components = []
        self.idx_components = [0] * n
        self.set_components()
        self.color = [0] * n

    def reset_color(self):
        self.color = [0] * self.num_nodes

    def dfs_set_component(self, current: int):
        self.idx_components[current] = self.num_components
        self.nodes_components[self.num_components - 1].append(current)
        for cand in self.edges[current]:
            if self.idx_components[cand] > 0:
                continue
            self.dfs_set_component(cand)

    def set_components(self):
        for i in range(self.num_nodes):
            if self.idx_components[i] > 0:
                continue
            self.num_components += 1
            self.nodes_components.append([])
            self.dfs_set_component(i)

    # i:idx of component, j: idx in component
    def dfs_count(self, i, j):
        if j == len(self.nodes_components[i]):
            return 1
        count = 0
        current_node = self.nodes_components[i][j]
        cand = {1, 2, 3}
        for k in self.edges[current_node]:
            cand.discard(self.color[k])
        for c in cand:
            self.color[current_node] = c
            count += self.dfs_count(i, j + 1)
            self.color[current_node] = 0
        return count

    def get_num_3coloring(self):
        if self.num_edges == 0:
            return 3**self.num_nodes
        elif self.num_edges == self.num_nodes * (self.num_nodes + 1) // 2:
            return 0
        else:
            counter = 1
            for i in range(self.num_components):
                self.reset_color()
                counter *= self.dfs_count(i, 0)
            return counter


class Tree(Graph):
    import sys
    sys.setrecursionlimit(10**6)

    def __init__(self, n: int, e: list):
        super(Tree, self).__init__(n, e)

    def dfs(self, current: int, prev: int):
        for cand in self.edges[current]:
            if cand == prev:
                continue
            #  Here, process will be written
            self.dfs(cand, current)

    def bfs(self):
        pass


class TreeCustomized(Tree):  # ABC198E
    import sys
    sys.setrecursionlimit(10**6)

    def __init__(self, n: int, e: list, c: list):
        super(TreeCustomized, self).__init__(n, e)
        self.values = c
        self.state = {c[0]}
        self.ans = [1]

    def dfs(self, current: int, prev: int):
        for cand in self.edges[current]:
            if cand == prev:
                continue
            c = self.values[cand]
            if c in self.state:
                self.dfs(cand, current)
            else:
                self.state.add(c)
                self.ans.append(cand + 1)
                self.dfs(cand, current)
                self.state.remove(c)


class LoopBitBruteForce:  # ABC_197_C
    def __init__(self):
        self.n = Inputs.inInt()
        self.a = Inputs.inInts()

    def solve(self):
        ans = 2**31
        for mask in range(1 << (self.n - 1)):
            val_xor = 0
            tmp = self.a[0]
            for i in range(1, self.n):
                if mask & 1 << (i - 1):
                    val_xor ^= tmp
                    tmp = 0
                tmp |= self.a[i]
            val_xor ^= tmp
            ans = min(ans, val_xor)
        return ans


def solve():
    # 入力
    N, Q = Inputs.inInts()
    ab = Inputs.inIntsN(N - 1)
    cd = Inputs.inIntsN(Q)
    # 求解
    g = Graph(N, ab)
    dist = g.dijkstra(0)
    ans = []
    for i in range(Q):
        d1 = dist[cd[i][0] - 1]
        d2 = dist[cd[i][1] - 1]
        if abs(d1 - d2) % 2 == 0:
            ans.append('Town')
        else:
            ans.append('Road')
    # 回答
    for a in ans:
        print(a)


if __name__ == "__main__":
    solve()
