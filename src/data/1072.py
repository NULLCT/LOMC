class INPUT:
    def __init__(self):
        self._l = open(0).read().split()
        self._length = len(self._l)
        self._index = 0
        return

    def stream(self, k=1, f=int, f2=False):
        assert (-1 < k)
        if self._length == self._index or self._length - self._index < k:
            raise Exception("There is no input!")
        elif f != str:
            if k == 0:
                ret = list(map(f, self._l[self._index:]))
                self._index = self._length
                return ret
            if k == 1 and not f2:
                ret = f(self._l[self._index])
                self._index += 1
                return ret
            if k == 1 and f2:
                ret = [f(self._l[self._index])]
                self._index += 1
                return ret
            ret = []
            for _ in [0] * k:
                ret.append(f(self._l[self._index]))
                self._index += 1
            return ret
        else:
            if k == 0:
                ret = list(self._l[self._index:])
                self._index = self._length
                return ret
            if k == 1 and not f2:
                ret = self._l[self._index]
                self._index += 1
                return ret
            if k == 1 and f2:
                ret = [self._l[self._index]]
                self._index += 1
                return ret
            ret = []
            for _ in [0] * k:
                ret.append(self._l[self._index])
                self._index += 1
            return ret


pin = INPUT().stream
"""
pin(number[default:1],f[default:int],f2[default:False])
if number==0 -> return left all
listを変数で受け取るとき、必ずlistをTrueにすること。
"""
from collections import deque
from sys import setrecursionlimit

setrecursionlimit(1000000)


def main():
    N, Q = pin(2)
    E = [[] for _ in [0] * N]
    for _ in [0] * (N - 1):
        a, b = pin(2)
        E[a - 1].append(b - 1)
        E[b - 1].append(a - 1)
    dq = deque()
    dq.append(0)
    check = [False] * N
    G = [[] for _ in [0] * N]
    while dq:
        q = dq.pop()
        check[q] = True
        for i in E[q]:
            if check[i]:
                continue
            G[q].append(i)
            dq.append(i)
    S = []
    F = [0] * N
    depth = [0] * N

    def dfs(v, d):
        F[v] = len(S)
        depth[v] = d
        S.append(v)
        for w in G[v]:
            dfs(w, d + 1)
            S.append(v)
        return

    dfs(0, 0)
    INF = (N, None)
    M = 2 * N
    M0 = 2**(M - 1).bit_length()
    data = [INF] * (2 * M0)
    for i, v in enumerate(S):
        data[M0 - 1 + i] = (depth[v], i)
    for i in range(M0 - 2, -1, -1):
        data[i] = min(data[2 * i + 1], data[2 * i + 2])

    def _query(a, b):
        yield INF
        a += M0
        b += M0
        while a < b:
            if b & 1:
                b -= 1
                yield data[b - 1]
            if a & 1:
                yield data[a - 1]
                a += 1
            a >>= 1
            b >>= 1
        return

    def query(u, v):
        fu = F[u]
        fv = F[v]
        if fu > fv:
            fu, fv = fv, fu
        return S[min(_query(fu, fv + 1))[1]]

    for _ in [0] * Q:
        c, d = pin(2)
        c -= 1
        d -= 1
        u = query(c, d)
        t = 2 * depth[u] - depth[c] - depth[d]
        if t % 2 == 0:
            print("Town")
        else:
            print("Road")
    return


main()
