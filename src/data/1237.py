import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder__bit_code = """
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x
"""

atcoder._bit = types.ModuleType('atcoder._bit')
exec(_atcoder__bit_code, atcoder._bit.__dict__)

_atcoder_segtree_code = """
import typing

# import atcoder._bit


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = atcoder._bit._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
"""

atcoder.segtree = types.ModuleType('atcoder.segtree')
atcoder.segtree.__dict__['atcoder'] = atcoder
atcoder.segtree.__dict__['atcoder._bit'] = atcoder._bit
exec(_atcoder_segtree_code, atcoder.segtree.__dict__)
SegTree = atcoder.segtree.SegTree

#!/usr/bin/env python3
# from atcoder.segtree import SegTree
from functools import reduce
from typing import *

ODDS = "Road"
EVEN = "Town"

INF = float("inf")


class ArgminData(NamedTuple):
    value: int
    index: int  # type: ignore


class EulerTour:
    def __init__(
        self,
        adj: List[List[int]],
        root: int = 0,
    ) -> None:
        self.N = len(adj)
        self.adj = adj
        self.root = root
        self.build()
        self.post_build()
        self.build_seg()

    def build(self) -> None:
        self.tour: List[int] = list()
        self.visited = [False] * self.N
        # prev[root] == rootにするか-1にするか迷う
        self.prev = [self.root] * self.N
        stack = [~self.root, self.root]
        while stack:
            src = stack.pop()
            if src >= 0:
                self.visited[src] = True
                self.tour.append(src)
                for dst in reversed(self.adj[src]):
                    if self.visited[dst]: continue
                    stack.append(~dst)
                    stack.append(dst)
                    self.prev[dst] = src
            else:
                self.tour.append(src)

    def post_build(self) -> None:
        self.enter = [-1] * self.N
        self.exit = [-1] * self.N
        self.tour_depth = [-1] * (2 * self.N)
        d = -1
        assert len(self.tour) == 2 * self.N
        for i in range(2 * self.N):
            if self.tour[i] >= 0:
                self.enter[self.tour[i]] = i
                d += 1
            else:
                self.exit[~self.tour[i]] = i
                d -= 1
            self.tour_depth[i] = d

    def build_seg(self) -> None:
        e = ArgminData(INF, -1)
        v = [ArgminData(self.tour_depth[i], i) for i in range(2 * self.N)]
        self.seg = SegTree(min, e, v)  # Range Min Query

    def LCA_depth(self, u: int, v: int) -> int:
        iu, iv = self.enter[u], self.enter[v]
        iu, iv = min(iu, iv), max(iu, iv)
        ans = self.seg.prod(iu, iv + 1).value
        return ans

    def depth(self, u: int) -> int:
        return self.tour_depth[self.enter[u]]

    def distance(self, u: int, v: int) -> int:
        return self.depth(u) + self.depth(v) - 2 * self.LCA_depth(u, v)

    def LCA(self, u: int, v: int) -> Tuple[bool, int]:
        iu, iv = self.enter[u], self.enter[v]
        iu, iv = min(iu, iv), max(iu, iv)
        index = self.seg.prod(iu, iv + 1).index
        current = self.tour[index]
        flag = current >= 0
        if flag:
            #            print(f"\x1b[31m[+]{self.prev[current]}->{current}\x1b[m")
            return flag, current
        else:
            #            print(f"\x1b[31m[-]{self.prev[~current]}->{current}\x1b[m")
            return flag, self.prev[~current]


# def solve(N: int, Q: int, a: List[int], b: List[int], c: List[int], d: List[int]) -> List[str]:
def solve(N, Q, a, b, c, d):
    adj = [list() for _ in range(N)]
    for i in range(N - 1):
        adj[a[i]].append(b[i])
        adj[b[i]].append(a[i])
    ET = EulerTour(adj, 0)
    for u, v in zip(c, d):
        dist = ET.distance(u, v)
        if dist % 2 == 1:
            print(ODDS)
        else:
            print(EVEN)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, Q = map(int, input().split())
    a = [None for _ in range(N - 1)]
    b = [None for _ in range(N - 1)]
    c = [None for _ in range(Q)]
    d = [None for _ in range(Q)]
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    for i in range(Q):
        c[i], d[i] = map(int, input().split())
        c[i] -= 1
        d[i] -= 1
    solve(N, Q, a, b, c, d)


if __name__ == '__main__':
    main()
