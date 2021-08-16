import math
import itertools
from decimal import Decimal
from functools import reduce
import collections
import bisect
import queue


def main():
    # n = int(input())
    # a,b = input().split()
    n, q = map(int, input().split())
    # c = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    # s_ = input()
    # c = [list(input()) for _ in range(h)]
    # m = int(input())
    # d = [list(map(int, input().split())) for _ in range(n)]
    # l = [int(input()) for _ in range(n)]
    # c = [input() for _ in range(h)]
    # mod = 10**9+7
    path = [[] for _ in range(n)]

    ab = [list(map(int, input().split())) for _ in range(n - 1)]
    cd = [list(map(int, input().split())) for _ in range(q)]

    for a, b in ab:
        path[a - 1].append(b - 1)
        path[b - 1].append(a - 1)

    que = queue.Queue()
    color = [-1] * n
    color[0] = 0
    que.put(0)
    while not que.empty():
        t = que.get()
        for i in path[t]:
            if color[i] == -1:
                color[i] = 1 - color[t]
                que.put(i)

    for c, d in cd:
        if color[c - 1] == color[d - 1]:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    main()
