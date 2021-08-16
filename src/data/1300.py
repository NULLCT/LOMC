class SegTree:
    X_unit = float("inf")
    X_f = min

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


def euler_tour(tree, root=1):
    N = len(tree) - 1
    seen = [-1] * (N + 1)
    parent = [0] * (N + 1)
    depth = [-1] * (N + 1)
    depth[parent[root]] = -1
    euler_order = []
    stack = [root]
    while stack:
        u = stack.pop()
        if u > 0:
            euler_order.append(u)
            depth[u] = depth[parent[u]] + 1
            stack.append(-u)
            seen[u] = 1
            for v in tree[u]:
                if seen[v] == -1:
                    parent[v] = u
                    stack.append(v)
                    seen[v] = 0
        else:
            euler_order.append(parent[-u])
            seen[-u] = 2
    euler_order.pop()
    first_appear = [-1] * (N + 1)
    for i, v in enumerate(euler_order):
        if first_appear[v] == -1:
            first_appear[v] = i
    return euler_order, first_appear, depth


#(depth, vertex)
def get_lca(a, b):
    pa, pb = first_appear[a], first_appear[b]
    if pa > pb:
        pa, pb = pb, pa
    return divmod(seg.fold(pa, pb + 1), offset)


def get_dist(a, b):
    d, c = get_lca(a, b)
    return depth[a] + depth[b] - 2 * d


def is_on_path(a, b, c):
    return dist(a, c) + dist(c, b) == dist(a, b)


def make_tree(N, edges):
    tree = [[] for _ in range(N + 1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    return tree


N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

tree = make_tree(N, AB)
euler_order, first_appear, depth = euler_tour(tree)
offset = N + 1
E = [depth[v] * offset + v for v in euler_order]
seg = SegTree(len(E))
seg.build(E)

for _ in range(Q):
    c, d = map(int, input().split())
    d = get_dist(c, d)
    if d % 2:
        print("Road")
    else:
        print("Town")
