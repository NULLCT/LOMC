import typing
import sys
import math
import collections
import bisect
import itertools
import heapq
import copy

# ===TEMPLATE==
# sys.setrecursionlimit(10**7+1)
# inf = float('inf')
inf = 10**20
mod = 10**9 + 7
# mod = 998244353


def ni():
    return int(sys.stdin.buffer.readline())


def ns():
    return map(int, sys.stdin.buffer.readline().split())


def na():
    return list(map(int, sys.stdin.buffer.readline().split()))


def na1():
    return list(map(lambda x: int(x) - 1, sys.stdin.buffer.readline().split()))


def nall():
    return list(map(int, sys.stdin.buffer.read().split()))


def flush():
    return sys.stdout.flush()


def nic():
    return int(sys.stdin.readline())


def nsc():
    return map(int, sys.stdin.readline().split())


def nac():
    return list(map(int, sys.stdin.readline().split()))


def na1c():
    return list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===
def main():
    n, q = ns()
    e = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = na1()
        e[a].append(b)
        e[b].append(a)

    dist = [inf for _ in range(n)]
    dist[0] = 0
    que = collections.deque()
    que.append([0, 0])
    while que:
        idx, d = que.popleft()
        for nidx in e[idx]:
            if dist[nidx] == inf:
                dist[nidx] = d + 1
                que.append([nidx, d + 1])

    for _ in range(q):
        ci, di = na1()
        res = dist[ci] - dist[di]
        print("Town" if res % 2 == 0 else "Road")


if __name__ == '__main__':
    main()
