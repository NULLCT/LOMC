import sys

sys.setrecursionlimit(10**8)
from typing import NamedTuple
from operator import itemgetter, attrgetter
from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import heapq
import bisect
import math


def main():
    N, Q = map(int, input().split())
    Edge = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        Edge[a].append(b)
        Edge[b].append(a)

    seen = [False] * N
    score = [-1] * N

    score[0] = 0
    stack = [0]

    while stack:
        v = stack.pop()
        seen[v] = True
        for u in Edge[v]:
            if seen[u]:
                continue
            score[u] = score[v] + 1
            stack.append(u)

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        v = abs(score[c] - score[d])

        if v % 2 == 0:
            ans = "Town"
        else:
            ans = "Road"
        print(ans)


if __name__ == "__main__":
    main()
