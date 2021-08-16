#!/usr/bin/env python3

from sys import setrecursionlimit, stdin
from typing import Dict, Iterable, Set

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


def bfs_dist_graph(start: int, size, graph: Dict[int, Set[int]]) -> int:
    dists = [-1] * size
    dists[start] = 0
    checked = set()
    checked.add(start)

    from collections import deque
    nexts = deque([(0, start)])
    while nexts:
        depth, now = nexts.popleft()
        dists[now] = depth
        checked.add(now)
        for next_ in graph[now]:
            if next_ not in checked:
                nexts.append((depth + 1, next_))

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

    dists = bfs_dist_graph(0, n, path)

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
