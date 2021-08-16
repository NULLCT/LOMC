n, q = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]

from collections import defaultdict

g = defaultdict(list)
for a, b in ab:
    g[a] += [b]
    g[b] += [a]


# Euler Tour
def dfs(u, d):
    # first visit
    vis = [-1] * (n + 1)
    # euler tour
    et = []
    que = [(-u, d), (u, d)]

    while len(que) > 0:
        u, d = que.pop()
        if u > 0:
            # 行きがけの処理
            vis[u] = len(et)
            et += [(u, d)]
            for v in g[u]:
                if vis[v] == -1:  # 未探索のみ
                    que += [(-v, d + 1)]  # 帰り
                    que += [(v, d + 1)]  # 行き
        else:
            # 帰りがけの処理
            et += [(u, d)]

    return vis, et


vis, et = dfs(1, 0)


class SegmentTree():
    def __init__(self, a):
        self.INF = float("inf")
        n = len(a)
        p = n.bit_length()
        aug = pow(2, p) - n
        a += [self.INF] * aug
        self.n = len(a)
        self.tree = [self.INF] * (2 * self.n - 1)

        # 葉の値をセット
        for i in range(self.n):
            j = i + self.n - 1
            self.tree[j] = a[i]

        # 葉に近い方から更新していく
        for j in range(self.n - 2, -1, -1):
            self.tree[j] = min(self.tree[j * 2 + 1], self.tree[j * 2 + 2])

    def update(self, i, x):
        # i番目はn-1+i番目
        j = i + self.n - 1
        self.tree[j] = x  # 新しい値
        while (j > 0):
            # 親を辿りながら更新
            j = (j - 1) // 2
            self.tree[j] = min(self.tree[j * 2 + 1], self.tree[j * 2 + 2])

    def rmq(self, a, b):
        k, l, r = 0, 0, self.n
        ans = self.INF
        stack = [(k, l, r)]

        while len(stack):
            k, l, r = stack.pop()
            if r <= a or b <= l:
                pass
            elif a <= l and r <= b:
                ans = min(ans, self.tree[k])
            else:
                stack.append((2 * k + 1, l, (l + r) // 2))
                stack.append((2 * k + 2, (l + r) // 2, r))

        return ans


a = [t for e, t in et]
st = SegmentTree(a)

for c, d in cd:
    vc, vd = vis[c], vis[d]
    dc, dd = a[vc], a[vd]

    #print(c,d,vc,vd,dc,dd)

    if vc > vd:
        tmp = vc
        vc = vd
        vd = tmp

    #continue
    #print(c, d, vc, vd)
    m = st.rmq(vc, vd + 1)

    dist = dc + dd - 2 * m

    if dist % 2 == 0:
        print("Town")
    else:
        print("Road")
