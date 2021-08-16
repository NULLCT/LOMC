import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext


def i_input():
    return int(input())


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def i_row(N):
    return [i_input() for _ in range(N)]


def i_row_list(N):
    return [i_list() for _ in range(N)]


def s_input():
    return input()


def s_map():
    return input().split()


def s_list():
    return list(s_map())


def s_row(N):
    return [s_input for _ in range(N)]


def s_row_str(N):
    return [s_list() for _ in range(N)]


def s_row_list(N):
    return [list(s_input()) for _ in range(N)]


def lcm(a, b):
    return a * b // gcd(a, b)


sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 10**9 + 7
num_list = []
str_list = []


def dfs(i, graph, dist, depth):
    depth += 1
    for j in graph[i]:
        if dist[j] == 0:
            dist[j] = depth
            dfs(j, graph, dist, depth)


def main():
    n, q = i_map()
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = i_map()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    query = i_row_list(q)
    dist = [0] * n

    dfs(0, graph, dist, 0)

    for a, b in query:
        if (dist[a - 1] + dist[b - 1]) % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
