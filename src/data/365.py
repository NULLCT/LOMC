#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt


def LI():
    return list(map(int, input().split()))


def LF():
    return list(map(float, input().split()))


def LI_():
    return list(map(lambda x: int(x) - 1, input().split()))


def II():
    return int(input())


def IF():
    return float(input())


def S():
    return input().rstrip()


def LS():
    return S().split()


def IR(n):
    return [II() for _ in range(n)]


def LIR(n):
    return [LI() for _ in range(n)]


def FR(n):
    return [IF() for _ in range(n)]


def LFR(n):
    return [LI() for _ in range(n)]


def LIR_(n):
    return [LI_() for _ in range(n)]


def SR(n):
    return [S() for _ in range(n)]


def LSR(n):
    return [LS() for _ in range(n)]


mod = 1000000007
inf = 1e10


#solve
def solve():
    N, Q = LI()
    xy = LIR(N - 1)
    ab = LIR(Q)
    field = [[] for i in range(N)]

    for x, y in xy:
        field[x - 1].append(y - 1)
        field[y - 1].append(x - 1)

    takasa = [-1] * N
    takasa[0] = 0
    par = [[None for i in range(20)] for k in range(N)]
    q = deque()
    q.append(0)
    par[0][0] = 0
    while q:
        oya = q.pop()

        for ko in field[oya]:
            if takasa[ko] < 0:
                takasa[ko] = takasa[oya] + 1
                q.append(ko)
                par[ko][0] = oya

    for j in range(18):
        for i in range(N):
            par[i][j + 1] = par[par[i][j]][j]

    for a, b in ab:
        a -= 1
        b -= 1
        ans = takasa[a] + takasa[b] + 1

        if takasa[a] > takasa[b]:
            a, b = b, a

        for i in range(18):
            if (takasa[b] - takasa[a]) & 1 << i:
                b = par[b][i]

        if a == b:
            tmp = ans - 2 * takasa[a]
        else:
            for i in range(17, -1, -1):
                if par[a][i] != par[b][i]:
                    a = par[a][i]
                    b = par[b][i]

            tmp = ans - 2 * takasa[par[a][0]]
        if tmp & 1:
            print("Town")
        else:
            print("Road")
    return


#main
if __name__ == '__main__':
    solve()
