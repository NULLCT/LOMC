import sys
from pprint import pprint
from typing import List
from collections import deque
import itertools
from bisect import bisect

input = sys.stdin.readline
sys.setrecursionlimit = 10**6

MOD = 10**9 + 7


def d():
    N, Q = map(int, input().split())
    paths = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        paths[a - 1].append(b - 1)
        paths[b - 1].append(a - 1)

    # pprint(paths)

    dist = []
    for _ in range(N):
        dist.append(-1)

    deq = deque()

    deq.append(0)

    dist[0] = 0

    while deq:
        i = deq.popleft()
        for j in paths[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                deq.append(j)

    # pprint(dist)

    def inspect(c, d):
        c -= 1
        d -= 1
        if dist[c] % 2 == dist[d] % 2:
            return 'Town'
        else:
            return 'Road'

    ans = []
    for _ in range(Q):
        c, d = map(int, input().split())
        ans.append(inspect(c, d))

    for i in ans:
        print(i)

    return


if __name__ == '__main__':
    d()
