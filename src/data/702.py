import sys, bisect, collections, copy, heapq, itertools, math, string
# import numpy as np
from functools import lru_cache


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


sys.setrecursionlimit(10**6)


def main():
    N, Q = LI()
    G = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b = LI()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    start = 0
    candidate = [start]
    distance = [0] * N
    done = [False] * N
    while candidate:
        p = candidate.pop()
        done[p] = True
        for next_p in G[p]:
            if done[next_p]:
                continue
            distance[next_p] = distance[p] + 1
            candidate.append(next_p)

    # print(distance)
    for _ in range(Q):
        start, goal = LI()
        start -= 1
        goal -= 1
        if abs(distance[start] - distance[goal]) % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
