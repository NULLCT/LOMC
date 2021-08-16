import sys
from collections import defaultdict
from itertools import groupby, permutations as pm, combinations as cm, product, combinations_with_replacement as cmrp

sys.setrecursionlimit(1000000)


def input():
    return sys.stdin.readline()[:-1]


def insp():
    return map(int, input().split())


def stsp():
    return input().split()


def solve():
    n, q = insp()
    graph = defaultdict(list)
    for i in range(n - 1):
        a, b = insp()
        graph[a].append(b)
        graph[b].append(a)

    qs = []
    for i in range(q):
        a, b = insp()
        qs.append((a, b))

    answers = ["Road"] * q
    start = 0
    stack = [1]
    dis = [0 for i in range(n + 1)]
    searched = [False for i in range(n + 1)]
    while stack:
        search = stack.pop()
        if searched[search]:
            continue
        searched[search] = True
        for t in graph[search]:
            dis[t] = (dis[search] + 1) % 2
            stack.append(t)

    for i, query in enumerate(qs):
        if dis[query[0]] == dis[query[1]]:
            answers[i] = "Town"

    print(*answers, sep="\n")
    return 0


if __name__ == "__main__":
    solve()
