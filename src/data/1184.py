import sys, os
from collections import deque, defaultdict
import math
import bisect

sys.setrecursionlimit(10**9)
INF = 1 << 64
MOD = 10**9 + 7


def main(f=sys.stdin):
    answer(deque(map(lambda s: s.rstrip(os.linesep), f.readlines())))


def dfs(r, l, i, t):
    for e in r[i]:
        if l[e] < 0:
            l[e] = t
            dfs(r, l, e, t + 1)


def answer(lines):
    # n = int(lines.popleft())
    # a, b = [int(s) for s in lines.popleft().split()]

    n, q = [int(s) for s in lines.popleft().split()]
    r = defaultdict(set)

    for i in range(n - 1):
        a, b = [int(s) - 1 for s in lines.popleft().split()]
        r[a].add(b)
        r[b].add(a)

    l = [-1] * n
    dfs(r, l, 0, 0)

    for i in range(q):
        c, d = [int(s) - 1 for s in lines.popleft().split()]
        print("Town" if l[c] % 2 == l[d] % 2 else "Road")


if 'debug' not in globals():
    main()
