from collections import deque
import sys
from typing import Any, List, Tuple, Dict, Set, Callable

sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
E = [tuple([int(s) for s in input().split()]) for _ in range(N - 1)]
C = [tuple([int(s) for s in input().split()]) for _ in range(Q)]
'''
N = 10 ** 5
Q = 0
E = [(i, i + 1) for i in range(1, N)]
C = []
'''


def calc():
    d_path = {i: [] for i in range(N)}
    for a, b in E:
        d_path[a - 1].append(b - 1)
        d_path[b - 1].append(a - 1)
    # EulerTourを構築
    visit_order = []
    F = [-1] * N  # visit_orderで最初に出現した位置
    depth = [-1] * N
    parent = [-1] * N
    stk = deque([(0, 0)])
    while stk:
        v, d = stk.pop()
        if depth[v] == -1:
            F[v] = len(visit_order)
            depth[v] = d
            visit_order.append(v)
            has_next = False
            for w in d_path[v]:
                if depth[w] == -1:
                    stk.append((w, d + 1))
                    parent[w] = v
                    has_next = True
            if not has_next:
                stk.append((parent[v], d - 1))
        else:
            visit_order.append(v)
            visited_all = True
            for w in d_path[v]:
                if F[w] == -1:
                    visited_all = False
                    break
            if visited_all and parent[v] != -1:
                stk.append((parent[v], d - 1))
    # LCAの前計算

    class SegTree:
        def __init__(self, n: int, init) -> None:
            self.N: int = 1
            while self.N < n:
                self.N *= 2
            self.init: int = init
            self.data: List[int] = [init] * (self.N * 2 + 1)

        # i: 0-index
        def update(self, i: int, v) -> None:
            i += self.N - 1
            self.data[i] = v
            while i > 0:
                i = (i - 1) // 2
                self.data[i] = min(self.data[i * 2 + 1], self.data[i * 2 + 2])

        # a, b: 0-index
        # bを含めない
        def query(self, a: int, b: int):
            return self._query(a, b, 0, 0, self.N)

        def _query(self, a: int, b: int, k: int, l: int, r: int) -> int:
            if r <= a or b <= l:
                return self.init
            if a <= l and r <= b:
                return self.data[k]
            m: int = (l + r) // 2
            return min(self._query(a, b, k * 2 + 1, l, m),
                       self._query(a, b, k * 2 + 2, m, r))

    segtree = SegTree(2 * N, (N, None))
    for i in range(len(visit_order)):
        segtree.update(i, (depth[visit_order[i]], i))
    ans = []
    for c, d in C:
        vo_c = F[c - 1]
        vo_d = F[d - 1]
        if vo_c > vo_d:
            vo_c, vo_d = vo_d, vo_c
        dep, lca = segtree.query(vo_c, vo_d)
        # print(depth[c - 1], depth[d - 1], depth[lca])
        distance = depth[c - 1] + depth[d - 1] - \
            2 * depth[visit_order[lca - 1]]
        ans.append('Town' if distance % 2 == 0 else 'Road')
    return '\n'.join(ans)


print(calc())
