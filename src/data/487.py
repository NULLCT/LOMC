n, q = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

# graph, n and root is necessary
idx = 0

root = 0


def dfs(start, graph):
    global idx
    par = [-1] * n
    depth = [-1] * n
    stack = []
    stack.append(~start)
    stack.append(start)
    depth[start] = 0
    euler = []
    left = [-1] * n
    right = [-1] * n
    while stack:
        v = stack.pop()
        if v >= 0:
            d = depth[v]
            euler.append(v)
            if left[v] == -1:
                left[v] = idx
            idx += 1
            for u in graph[v]:
                if par[v] == u:
                    continue
                par[u] = v
                depth[u] = d + 1
                stack.append(~u)
                stack.append(u)
        else:
            a = ~v
            euler.append(par[a])
            if right[a] == -1:
                right[a] = idx
            idx += 1

    return euler, left, right, depth


euler, left, right, depth = dfs(root, graph)

depths = [depth[v] for v in euler]


class SegmentTree:
    # SEG木は1-index
    # Aに関しては0-index

    def __init__(self, n, ele, func):  # Aは0-idx
        self.n = n
        self.ele = ele
        self.func = func
        self.num = 2**((self.n - 1).bit_length())
        self.SEG = [self.ele] * (2 * self.num)

    def search(self, idx):
        return self.SEG[idx + self.num]

    def initialize(self, A):
        for i in range(self.n):
            self.SEG[i + self.num] = A[i]
        for i in range(self.num - 1, 0, -1):
            self.SEG[i] = self.func(self.SEG[2 * i], self.SEG[2 * i + 1])

    # 1点更新
    def set(self, idx, val):
        idx += self.num
        self.SEG[idx] = val
        idx //= 2
        while idx:
            self.SEG[idx] = self.func(self.SEG[2 * idx], self.SEG[2 * idx + 1])
            idx //= 2

    # 区間取得
    def query(self, left, right):
        # 開区間
        resleft = self.ele
        resright = self.ele
        left += self.num
        right += self.num
        while right - left > 0:
            if left % 2 == 1:
                resleft = self.func(resleft, self.SEG[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                resright = self.func(resright, self.SEG[right])
            left //= 2
            right //= 2
        return self.func(resleft, resright)


# 初期条件
def func(a, b):
    return min(a, b)


ele = 1 << 40

ST = SegmentTree(len(euler), ele, func)
ST.initialize(depths)

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    C = depth[c]
    D = depth[d]
    if C > D:
        c, d = d, c
        C = depth[c]
        D = depth[d]
    dd = ST.query(c, d + 1)
    dist = D + C - 2 * dd
    if dist % 2:
        print("Road")
    else:
        print("Town")
