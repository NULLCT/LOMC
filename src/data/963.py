import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class UnionFindTree:
    __all__ = ['root', 'merge', 'same', 'size']

    def __init__(self, maxsize=10**6):
        assert (maxsize > 0)
        self._n = maxsize
        self._parent_or_size = [-1] * maxsize

    def root(self, a):
        assert (0 <= a < self._n)
        pos = a
        children = []
        while self._parent_or_size[pos] >= 0:
            children.append(pos)
            pos = self._parent_or_size[pos]
        else:
            root_pos = pos
        for child_pos in children:
            self._parent_or_size[child_pos] = root_pos
        return root_pos

    def merge(self, a, b):
        assert (0 <= a < self._n)
        assert (0 <= b < self._n)
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a == root_b:
            return True
        else:
            if -self._parent_or_size[root_a] > -self._parent_or_size[root_b]:
                root_a, root_b = root_b, root_a
            self._parent_or_size[root_b] += self._parent_or_size[root_a]
            self._parent_or_size[root_a] = root_b
            return False

    def same(self, a, b):
        assert (0 <= a < self._n)
        assert (0 <= b < self._n)
        root_a = self.root(a)
        root_b = self.root(b)
        return root_a == root_b

    def size(self, a):
        assert (0 <= a < self._n)
        root_a = self.root(a)
        return -self._parent_or_size[root_a]


n, q = map(int, input().strip().split())
e = [[] for _ in range(n)]
for _ in range(n - 1):
    aa, bb = map(int, input().strip().split())
    e[aa - 1].append(bb - 1)
    e[bb - 1].append(aa - 1)

#print("e", e)

ut = UnionFindTree(maxsize=n)
depth = [-1] * n
from collections import deque

depth[0] = 0
que = deque([])
for x in e[0]:
    depth[x] = 1
    ut.merge(0, x)
    que.append(x)

while len(que) > 0:
    p = que.pop()
    for x in e[p]:
        if ut.same(0, x):
            continue
        depth[x] = depth[p] + 1
        ut.merge(0, x)
        que.append(x)

#print(depth)

for _ in range(q):
    c, d = map(int, input().strip().split())
    if abs(depth[c - 1] - depth[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
