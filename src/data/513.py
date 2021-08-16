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


from heapq import heappop, heappush


def dijkstra(start: int, n: int, edges, *, inf=INF):
    """
    単一始点最短経路問題を Dijkstra 法で解く
    計算量は O((E+V)log(V))
    Ref: https://mirucacule.hatenablog.com/entry/2020/05/21/124026

    start: 始点のインデックス
    n: ノード数
    edges: {edge_from: {edge_to: cost, ...}, ...} の形式の辞書
    返し値: startからそれぞれの点への最短経路問題を解いたときの回答のリスト
    """
    dists = [inf] * n
    hq = [(0, start)]
    dists[start] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to_, cost in edges[v].items():
            if seen[to_] is False and dists[v] + cost < dists[to_]:
                dists[to_] = dists[v] + cost
                heappush(hq, (dists[to_], to_))

    return dists


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

    edges = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        edges[i][i] = 0

    for a in range(n):
        for b in path[a]:
            edges[a][b] = 1
            edges[b][a] = 1

    dists = dijkstra(0, n, edges)

    for _ in range(q):
        c, d = inputs()
        c -= 1
        d -= 1
        d = dists[c] + dists[d]
        if d % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
