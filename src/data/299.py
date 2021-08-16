class segtree:
    """
    Segment tree
    Store value as object type and optional function for binary operarion.
    "get" function return a value by binary operarion result. O(logN)
    "update" function update tree's a value. O(logN)

    Attributes
    ----------
    n : int
        Number of elements
    identity element_func : func
        identity_element for initialization
        if operator is * and identiry element is e, e * A = A and A * e = A
    binary_operation_func : func
        function for binary operation x and y
        function must have associative law
        if operator is *, (A * B) * C = A * (B * C)

    Methods
    -------
    update(i, x)
        update tree[i] value to x
    get(a, b)
        get value from [a, b)
        include a but not include b, return a merged value
    """
    def __init__(self, n: int, identity_element_func, binary_operation_func):
        """
        Constructer(Initialize parameter in this class)

        Parameters
        ----------
        n : int
            Number of elements
        identity_element_func : func
            identity element for initialization
            if operator is * and identiry element is e, e * A = A and A * e = A
        binary_operation_func : func
            function for binary operation x and y
            function must have associative law
            if operator is *, (A * B) * C = A * (B * C)
        """
        self.n = n
        self.identity = identity_element_func
        self.binary = binary_operation_func
        n2 = 1  # n2はnより大きい2の冪数
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        self.tree = [identity_element_func() for _ in range(n2 << 1)]

    def update(self, index: int, x: int):
        """
        Update segment-tree's a value and update segment-tree's tree

        Parameters
        ----------
        index : int
            index of update value
        x : int
            new value
        """
        index += self.n2
        self.tree[index] = self.binary(self.tree[index], x)
        while index > 1:
            # (index ^ 1) はiと1の排他的論理和(XOR)
            x = self.binary(x, self.tree[index ^ 1])
            index >>= 1  # 右ビットシフトで親ノードのインデックスへ移動
            self.tree[index] = self.binary(self.tree[index], x)

    def get(self, a: int, b: int) -> int:
        """
        Get a specific value by result of binary operation from interval [a, b)

        Parameters
        ----------
        a, b : int
            index of interval
            this is hald open interval, this interval include a but not b
        """
        result = self.identity()
        q = [(1, 0, self.n2)]
        while q:
            k, left, right = q.pop()
            if a <= left and right <= b:
                result = self.binary(result, self.tree[k])
                continue
            m = (left + right) // 2
            k <<= 1
            if a < m and left < b:
                q.append((k, left, m))
            if a < right and left < m:
                q.append((k + 1, m, right))
        return result


N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda n: int(n) - 1, input().split())
    edge[x].append(y)
    edge[y].append(x)  # 有向グラフならこの行は消す!!
INF = 10**18

first_seen_i_on_tour = [-1] * N
height_tour = segtree(N, lambda: INF, min)
cnt = 0
queue = [(0, 0)]
while queue:
    now, depth = queue.pop()
    if first_seen_i_on_tour[now] != -1:
        continue
    first_seen_i_on_tour[now] = cnt
    height_tour.update(cnt, depth)
    cnt += 1

    depth += 1
    for n_node in edge[now]:
        if first_seen_i_on_tour[n_node] != -1:
            continue
        queue.append((n_node, depth))

for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    left, right = sorted(first_seen_i_on_tour[i] for i in (c, d))
    lca = height_tour.get(left, right)
    ans = sum(height_tour.get(i, i + 1) for i in (left, right))
    ans -= 2 * height_tour.get(lca, lca + 1)
    if ans & 1:
        print("Road")
    else:
        print("Town")
