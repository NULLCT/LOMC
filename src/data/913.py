#!/usr/bin/env python3
from collections import deque
import sys

# def dfs(start):
#     reach = deque([0])
#     distance = [-1 for _ in range(N)]
#     distance[start] = 0
#     while reach:
#         _from = reach.pop(0)
#         for _to in G[_from]:
#             if not(_to in reach) and distance[_to] == -1:
#                 reach.append(_to)
#                 distance[_to] = distance[_from]+1
#     return(distance)


def main():

    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        G[x].append(y)
        G[y].append(x)

    reach = deque([0])
    distance = [-1 for _ in range(N)]
    distance[0] = 0
    while reach:
        _from = reach.pop()
        for _to in G[_from]:
            if not (_to in reach) and distance[_to] == -1:
                reach.append(_to)
                distance[_to] = distance[_from] + 1

    for i in range(Q):
        c, d = map(int, input().split())
        if (distance[c - 1] - distance[d - 1]) % 2:
            print('Road')
        else:
            print('Town')


if __name__ == '__main__':
    main()
