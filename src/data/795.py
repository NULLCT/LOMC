#!/usr/bin/env python3

from sys import setrecursionlimit, stdin
from typing import Iterable

INF: int = 2**62
MOD: int = 10**9 + 7

setrecursionlimit(10**6)


def inputs(type_=int):
    ins = input().split(' ')
    ins = [x for x in ins if x != '']

    if isinstance(type_, Iterable):
        return [t(x) for t, x in zip(type_, ins)]
    else:
        return list(map(type_, ins))


def input_(type_=int):
    a, = inputs(type_)
    return a


inputi = input_


def inputstr():
    return input_(str)


# b/aの切り上げ
def ceil(b, a):
    return (a + b - 1) // a


def answer(res) -> None:
    print(res)
    exit()


def compute():
    return


class UnionFind:
    """
    Ref: https://qiita.com/tefuxu/items/e9f99b6eefc3a7f76cc9
    ・自身が子のとき, 親ノード番号を格納する。自身が根のとき, ノード数を負の数で格納する
    ・負の数のときは自身が根であり, その絶対値がその木のノード数を表す
    """
    def __init__(self, n):
        # 親ノードを-1に初期化する
        self.parents = [-1] * n

    # 根を返す
    def find_root(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find_root(self.parents[x])
            return self.parents[x]

    # 同じ要素かどうか
    def are_same(self, x: int, y: int) -> bool:
        return self.find_root(x) == self.find_root(y)

    # xとyの木を併合する
    def union(self, x: int, y: int) -> None:
        # x,yの根をX,Yとする
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        # 根が同じなら結合済み
        if root_x == root_y:
            return

        # ノード数が多い方をXとする
        if self.parents[root_x] > self.parents[root_y]:
            root_x, root_y = root_y, root_x

        # XにYのノード数を足す
        self.parents[root_x] += self.parents[root_y]
        # Yの根を X(>0) とする
        self.parents[root_y] = root_x

    # 木のサイズ
    def size(self, x: int) -> int:
        return self.parents[self.find_root(x)] * -1


def main():
    n, q = inputs()
    from collections import defaultdict
    path = defaultdict(set)

    # print(n)
    for _ in range(n - 1):
        a, b = inputs()
        a -= 1
        b -= 1
        path[a].add(b)
        path[b].add(a)

    uf = UnionFind(n)
    for i in range(n):
        for j in path[i]:
            for k in path[j]:
                if k in path[i]:
                    continue
                else:
                    uf.union(i, k)

    # print(q)
    for _ in range(q):
        c, d = inputs()
        c -= 1
        d -= 1
        if uf.find_root(c) == uf.find_root(d):
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
