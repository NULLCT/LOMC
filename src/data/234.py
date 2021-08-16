# region Template
# fmt: off
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque, defaultdict


# from itertools import combinations, permutations, accumulate, groupby, product
# from bisect import bisect_left,bisect_right
# from heapq import heapify, heappop, heappush
# from math import floor, ceil ,factorial, gcd
# from operator import itemgetter
# from copy import deepcopy
def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


def SI():
    return input().rstrip()


def printns(x):
    print('\n'.join(x))


def printni(x):
    print('\n'.join(list(map(str, x))))


inf = 10**17
mod = 10**9 + 7
#mod =998244353


def INT():
    return int(sys.stdin.readline().rstrip())


def LINT():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def STR():
    return sys.stdin.readline().rstrip()


def LSTR():
    return list(sys.stdin.readline().rstrip().split())


# fmt: on
# endregion Template


def main():
    N, Q = MI()
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = MI()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    dist = [-1] * N
    dist[0] = 0
    que = deque([])
    que.append(0)

    while que:
        cur = que[0]
        que.popleft()
        for next in G[cur]:
            if dist[next] != -1:
                continue
            dist[next] = dist[cur] + 1
            que.append(next)

    for _ in range(Q):
        c, d = MI()
        c -= 1
        d -= 1
        if (dist[c] - dist[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
