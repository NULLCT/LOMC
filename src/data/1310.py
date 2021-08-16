import sys

readline = sys.stdin.readline


class HLD:
    def __init__(self, Edge):
        self.N = len(Edge)
        self.nxt = [0] * self.N
        self.In = [0] * self.N
        self.Out = [0] * self.N
        self.order = []
        self.par = [-1] * self.N

        Cld = Edge[:]
        size = [1] * self.N
        used = set()
        num = [0] * self.N
        self.dist = [0] * self.N
        for i in range(self.N):
            if i in used:
                continue
            used.add(i)
            stack = [~i, i]
            while stack:
                vn = stack.pop()
                if vn >= 0:
                    for idx in range(len(Cld[vn])):
                        vf = Cld[vn][idx]
                        used.add(vf)
                        self.par[vf] = vn
                        num[vf] = idx
                        Cld[vf].remove(vn)
                        stack.append(~vf)
                        stack.append(vf)
                elif ~vn != i:
                    vn = ~vn
                    pn = self.par[vn]
                    size[pn] += size[vn]
                    if size[Cld[pn][0]] < size[vn]:
                        Cld[pn][0], Cld[pn][num[vn]] = Cld[pn][
                            num[vn]], Cld[pn][0]

            t = 0
            stack = [~i, i]
            while stack:
                vn = stack.pop()
                if vn >= 0:
                    self.order.append(vn)
                    self.In[vn] = t
                    t += 1
                    for vf in Cld[vn][::-1]:
                        self.nxt[vf] = self.nxt[vn] if Cld[vn][0] == vf else vf
                        stack.append(~vf)
                        stack.append(vf)
                        self.dist[vf] = 1 + self.dist[vn]
                else:
                    vn = ~vn
                    self.Out[vn] = t

    def pathv(self, u, v):
        while True:
            if self.In[u] > self.In[v]:
                u, v = v, u
            l = max(self.In[self.nxt[v]], self.In[u])
            r = 1 + self.In[v]
            yield l, r
            if self.nxt[u] == self.nxt[v]:
                return
            v = self.par[self.nxt[v]]

    def pathe(self, u, v):
        #辺の情報を子供に持たせる
        while True:
            if self.In[u] > self.In[v]:
                u, v = v, u
            if self.nxt[u] == self.nxt[v]:
                yield self.In[u] + 1, self.In[v] + 1
                return
            yield self.In[self.nxt[v]], self.In[v] + 1
            v = self.par[self.nxt[v]]

    def subtree(self, u):
        return self.In[u], self.Out[u]

    def lca(self, u, v):
        while True:
            if self.In[u] > self.In[v]:
                u, v = v, u
            if self.nxt[u] == self.nxt[v]:
                return u
            v = self.par[self.nxt[v]]


def parorder(Edge, p):
    N = len(Edge)
    par = [0] * N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return par, order


def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res


N, Q = map(int, readline().split())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

T = HLD(Edge)

Ans = [None] * Q
for qu in range(Q):
    c, d = map(int, readline().split())
    c -= 1
    d -= 1

    l = T.lca(c, d)

    dd = T.dist[c] + T.dist[d] - 2 * T.dist[l]
    Ans[qu] = "Town" if dd % 2 == 0 else "Road"

print("\n".join(map(str, Ans)))
