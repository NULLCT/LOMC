from collections import deque
import sys
import math
import heapq
import random
import itertools


def gs():
    return sys.stdin.readline()


def gd():
    return float(sys.stdin.readline())


def gi():
    return int(sys.stdin.readline())


def gia():
    return list(map(int, sys.stdin.readline().split()))


def gsa():
    return sys.stdin.readline().split()


def eratoratenes(n):
    hurui = [True] * (n + 1)
    hurui[0] = False
    hurui[1] = False
    for i in range(2, n + 1):
        if (hurui[i] == False): continue
        if (i * i > n): break
        for j in range(2 * i, n + 1, i):
            hurui[j] = False


def zAlgo(S):
    n = len(S)
    if (n == 0): return []
    c = 0
    z = [0] * n
    for i in range(1, n):
        if (i + z[i - c] < c + z[c]):
            z[i] = z[i - c]
        else:
            j = max(0, c + z[c] - i)
            while (i + j < n and S[j] == S[i + j]):
                j += 1
            z[i] = j
            c = i

    return z


def floorSum(n, m, a, b):
    ans = 0
    if (a >= m):
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if (b >= m):
        ans += n * (b // m)
        b %= m

    yMax = (a * n + b) // m
    xMax = (yMax * m - b)
    if (yMax == 0): return ans
    ans += (n - (xMax + a - 1) // a) * yMax
    ans += floorSum(yMax, a, m, (a - xMax % a) % a)
    return ans


def ceil_pow2(n):
    x = 0
    while ((1 << x) < n):
        x += 1
    return x


def uclid(m, n):
    if (n == 0):
        return m
    else:
        return uclid(n, m % n)


#拡張ユークリッドの互除法
def invGcd(a, b):
    a %= b
    if a == 0: return b, 0
    s, t = b, a
    m0, m1 = 0, 1

    while (t):
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0

    if m0 < 0: m0 += b // s
    return s, m0


#約数取得
def yakusu(n):
    l = []
    for i in range(1, n + 1):
        if (i * i > n):
            break
        if (n % i == 0):
            l.append(i)
            if (n / i != i):
                l.append(n // i)

    return l


def insuB(n):
    l = []
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            l.append(i)
            n = n // i
        else:
            i += 1

    if (n != 1):
        l.append(n)

    return l


def insuBm(n):
    m = dict()
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            v = m.get(i, 0)
            m[i] = v + 1
            n = n // i
        else:
            i += 1

    if (n != 1):
        v = m.get(i, 0)
        m[i] = v + 1

    return m


# s進数で表した時の文字列
def Nsin(n, s):
    if (n == 0):
        return "0"

    l = []
    while (n != 0):
        a = n % s
        l.append(str(a))
        n = (n - a) // s

    sb = ''.join(l)
    return sb[::-1]


KAIJO_DP = [0] * 4000000


def kaijo(n, mod):
    if (n <= 1):
        return 1
    if (KAIJO_DP[n] != 0):
        return KAIJO_DP[n]
    ans = n * kaijo(n - 1, mod)
    ans %= mod
    KAIJO_DP[n] = ans
    return ans


def combi(n, m, mod):
    if (n < m):
        return 0

    nk = kaijo(n, mod)
    mk = kaijo(m, mod)
    nmk = kaijo(n - m, mod)
    bunbo = nmk * mk
    bunbo %= mod
    bunbo = pow(bunbo, mod - 2, mod)
    ans = nk * bunbo
    ans %= mod
    return ans


def isP(n):
    if (n == 1):
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True


def nextCombination(sub):
    x = sub & (-sub)
    y = sub + x
    return (((sub & ~y) // x) >> 1) | y


def topologicalSort(G):
    result = []
    inn = [0] * len(G)

    for es in G:
        for e in es:
            inn[e] += 1

    deq = deque()
    for i in range(len(G)):
        if (inn[i] == 0):
            deq.append(i)

    while (len(deq) != 0):
        v = deq.popleft()
        result.append(v)
        es = G[v]
        for e in es:
            inn[e] -= 1
            if (inn[e] == 0):
                deq.append(e)

    return result


class FenwickTree:
    def __init__(self, n):
        self.N = n
        self.data = [0] * n

    def add(self, p, x):
        if (p < 0 or p >= self.N):
            return None

        p += 1
        while (p <= self.N):
            self.data[p - 1] += x
            p += p & -p

    def get(self, l, r):
        if (l < 0 or l > r or r > self.N):
            return -(1 << 64)

        return self._innerSum(r) - self._innerSum(l)

    def _innerSum(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r

        return s


class FenwickTreeImos:
    def __init__(self, n):
        self.fw = FenwickTree(n + 1)

    def add(self, s, t, x):
        self.fw.add(s, x)
        self.fw.add(t, -x)

    def get(self, i):
        return self[i]

    def __getitem__(self, key):
        return self.fw.get(0, key + 1)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = [1] * n

    def find(self, n):
        if (n != self.parent[n]):
            self.parent[n] = self.find(self.parent[n])

        return self.parent[n]

    def union(self, n1, n2):
        r1 = self.find(n1)
        r2 = self.find(n2)
        if (self.rank[r1] > self.rank[r2]):
            self.parent[r2] = r1
            self.count[r1] = self.count[r1] + self.count[r2]
        elif (self.rank[r1] < self.rank[r2]):
            self.parent[r1] = r2
            self.count[r2] = self.count[r1] + self.count[r2]
        elif (r1 != r2):
            self.parent[r2] = r1
            self.rank[r1] += 1
            self.count[r1] = self.count[r1] + self.count[r2]

    def getRunk(self, n):
        return self.rank[n]

    def getCount(self, n):
        return self.count[self.find(n)]

    def getKindNum(self):
        ret = 0
        for i in range(len(self.parent)):
            if (self.parent[i] == i):
                ret += 1

        return ret

    def same(self, n1, n2):
        return self.find(n1) == self.find(n2)

    def grouping(self):
        m = dict()
        for i in range(len(self.parent)):
            p = self.find(i)
            l = m.get(p, [])
            l.append(i)
            m[p] = l
        return m


class Edge:
    def __init__(self, f, t, c):
        self._from = f
        self._to = t
        self._cost = c

    def getStart(self):
        return self._from

    def getEnd(self):
        return self._to

    def getDistance(self):
        return self._cost

    def setDistance(self, c):
        self._cost = c


class Graph:
    def __init__(self, n):
        self.gla = []
        self.prev = [-1] * n
        for i in range(n):
            self.gla.append([])

    def addEdge(self, u, v, l):
        e = Edge(u, v, l)
        self.gla[u].append(e)

    def removeEdge(self, u, v):
        l = self.gla[u]
        for edge in l:
            if (edge.getStart() == u and edge.getEnd() == v):
                l.remove(edge)

    def changeLength(self, u, v, d):
        l = self.gla[u]
        for edge in l:
            if (edge.getStart() == u and edge.getEnd() == v):
                edge.setDistance(d)
                break

    def getVertexNum(self):
        return len(self.gla)

    def getEdgeLength(self, u, v):
        l = self.gla[u]
        for edge in l:
            if (edge.getStart() == u and edge.getEnd() == v):
                return edge.getDistance()

        return 1 << 64

    def dijkstra(self, start):
        d = [1 << 64] * self.getVertexNum()
        d[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        self.prev[start] = -1
        while (len(q) != 0):
            p = heapq.heappop(q)
            if (p[0] > d[p[1]]):
                continue
            el = self.gla[p[1]]
            for edge in el:
                to = edge.getEnd()
                fr = edge.getStart()
                cost = edge.getDistance()
                if (d[to] > d[fr] + cost):
                    d[to] = d[fr] + cost
                    self.prev[to] = fr
                    heapq.heappush(q, (d[to], to))

        return d

    def getPath(self, v):
        path = []
        while (v != -1):
            path.append(v)
            v = self.prev[v]

        path.reverse()
        return path


class StringUtil:
    def __init__(self, S):
        self.S = S
        self.n = len(S)
        self.rank = [-1] * (self.n + 1)
        self.k = 1

    def _compareSa(self, i, j):
        if (self.rank[i] != self.rank[j]):
            return self.rank[i] < self.rank[j]
        else:
            ri = -1
            rj = -1
            if (i + self.k <= self.n):
                ri = self.rank[i + self.k]
            if (j + self.k <= self.n):
                rj = self.rank[j + self.k]
            return ri < rj

    def _comkey(self, i):
        r1 = self.rank[i]
        r2 = self.rank[i + self.k] if i + self.k <= self.n else -1
        return (r1, r2)

    def makeSa(self):
        sa = [0] * (self.n + 1)
        for i in range(len(sa)):
            sa[i] = i
            if (i < self.n):
                self.rank[i] = ord(self.S[i])

        self.k = 1
        tmp = [0] * (self.n + 1)
        while (self.k <= self.n):
            sa.sort(key=lambda x: self._comkey(x))

            tmp[sa[0]] = 0
            for i in range(1, self.n + 1):
                tmp[sa[i]] = tmp[sa[i - 1]]
                if (self._compareSa(sa[i - 1], sa[i])):
                    tmp[sa[i]] += 1
            for i in range(self.n + 1):
                self.rank[i] = tmp[i]
            self.k *= 2

        return sa

    def makeLcp(self, sa):
        for i in range(self.n + 1):
            self.rank[sa[i]] = i

        h = 0
        lcp = [0] * self.n
        for i in range(self.n):
            j = sa[self.rank[i] - 1]
            if (h > 0): h -= 1
            while (j + h < self.n and i + h < self.n):
                if (self.S[j + h] != self.S[i + h]): break
                h += 1

            lcp[self.rank[i] - 1] = h

        return lcp


class SegTree:
    def __init__(self, v, op, e):
        self.n = len(v)
        self.log = ceil_pow2(self.n)
        self.size = 1 << self.log
        self.op = op
        self.e = e
        self.d = [e] * (2 * self.size)
        for i in range(self.n):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def setVal(self, p, x):
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def getVal(self, p):
        return self.d[p + self.size]

    def prod(self, l, r):
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while (l < r):
            if (l & 1 != 0):
                sml = self.op(sml, self.d[l])
                l += 1
            if (r & 1 != 0):
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1

        return self.op(sml, smr)

    def allProd(self):
        return self.d[1]

    def maxRight(self, l, f):
        if (l == self.n): return self.n
        l += self.size
        sm = self.e
        while True:
            while (l % 2 == 0):
                l >>= 1
            if (not f(self.op(sm, self.d[l]))):
                while (l < self.size):
                    l = 2 * l
                    if (f(self.op(sm, self.d[l]))):
                        sm = self.op(sm, self.d[l])
                        l += 1

                return l - self.size

            sm = self.op(sm, self.d[l])
            l += 1
            if ((l & -l) != l): break

        return self.n

    def minLeft(self, r, f):
        if (r == 0): return 0
        r += self.size
        sm = self.e
        while (True):
            r -= 1
            while (r > 1 and r % 2 == 1):
                r >>= 1
            if (not f(self.op(self.d[r], sm))):
                while (r < self.size):
                    r = 2 * r + 1
                    if (f(self.op(self.d[r], sm))):
                        sm = self.op(self.d[r], sm)
                        r -= 1

                return r + 1 - self.size

            sm = self.op(self.d[r], sm)
            if ((r & -r) != r): break

        return 0

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])


class Ruiseki2d:
    def __init__(self, A):
        self.A = A
        self.H = len(A)
        self.W = len(A[0])
        self.S = [[0] * (self.W + 1) for i in range(self.H + 1)]
        for i in range(self.H):
            for j in range(self.W):
                self.S[i + 1][j + 1] = self.S[i + 1][j] + self.A[i][j]

        for i in range(self.H):
            for j in range(self.W + 1):
                self.S[i + 1][j] = self.S[i + 1][j] + self.S[i][j]

    def getSum(self, i, j, h, w):
        return self.S[i + h][j + w] - self.S[i][j + w] - self.S[
            i + h][j] + self.S[i][j]


class Gyoretu:
    def __init__(self, A, mod):
        self.N = len(A)
        self.A = A
        self.mod = mod
        E = [[0] * self.N for i in range(self.N)]
        for i in range(self.N):
            E[i][i] = 1

        self.Ap = [E, self.A]
        for i in range(60):
            lA = self.Ap[len(self.Ap) - 1]
            nA = self.multiA(lA, lA)
            self.Ap.append(nA)

    def multiA(self, A, B):
        ans = [[0] * self.N for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                tv = 0
                for k in range(self.N):
                    tv += A[i][k] * B[k][j]
                    tv %= self.mod
                ans[i][j] = tv

        return ans

    def powA(self, p):
        ans = self.Ap[0]
        for i in range(len(self.Ap) - 1):
            if (((p >> i) & 1) == 1):
                ans = self.multiA(ans, self.Ap[i + 1])

        return ans


def main_():
    N, Q = gia()
    depth = [-1] * N
    G = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = gia()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    depth[0] = 0
    deq = deque()
    deq.append(0)
    while (len(deq) > 0):
        v = deq.popleft()
        es = G[v]
        for i in range(len(es)):
            e = es[i]
            if (depth[e] >= 0): continue
            depth[e] = depth[v] + 1
            deq.append(e)

    for i in range(Q):
        c, d = gia()
        c -= 1
        d -= 1
        V = depth[c] + depth[d]
        if (V % 2 == 0):
            print("Town")
        else:
            print("Road")

    #print(ans)


main_()
