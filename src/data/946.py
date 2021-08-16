import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
e = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

eulbase = pow(10, 6)
lime = [[] for _ in range(N + 1)]
limevis = [0] * (N + 1)


def limitedge():
    global limevis
    global lime
    limevis[1] = 1
    s = [1]
    while len(s):
        x = s.pop()
        for y in e[x]:
            if limevis[y]: continue
            lime[x].append(y)
            limevis[y] = 1
            s.append(y)


euler = []
depth = [0] * (N + 1)
table = [0] * (N + 1)


def eulerdfs():
    global euler
    global depth
    global table
    s = [1]
    while len(s):
        x = s.pop()
        if x >= 0:
            euler.append(depth[x] * eulbase + x)
            for y in lime[x]:
                s.append(~x)
                s.append(y)
                depth[y] = depth[x] + 1
        else:
            euler.append(depth[~x] * eulbase + ~x)


limitedge()
eulerdfs()
for i in range(len(euler) - 1, -1, -1):
    table[euler[i] % eulbase] = i


class SparseTable:
    def calc(self, x, y):
        return min(x, y)

    def __init__(self, n, init_val, ide_ele):
        self.n = n
        k = n.bit_length()
        self.k = k
        self.ide_ele = ide_ele
        self.log_table = [[ide_ele] * n for _ in range(k + 1)]
        for i in range(n):
            self.log_table[0][i] = init_val[i]
        for i in range(k):
            d = 1 << i
            for j in range(n):
                if j + d >= n: break
                self.log_table[i + 1][j] = self.calc(self.log_table[i][j],
                                                     self.log_table[i][j + d])

    def query(self, l, r):
        d = r - l
        if d < 0: return self.ide_ele
        if d == 1: return self.log_table[0][l]
        m = d.bit_length() - 1
        return self.calc(self.log_table[m][l], self.log_table[m][r - (1 << m)])


st = SparseTable(len(euler), euler, N * eulbase)

for _ in range(Q):
    u, v = map(int, input().split())
    if table[u] > table[v]: u, v = v, u
    root = st.query(table[u], table[v]) % eulbase
    d = depth[u] + depth[v] - depth[root] * 2
    if d % 2: print("Road")
    else: print("Town")
