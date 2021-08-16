import bisect, collections, copy, heapq, itertools, math, string, sys, queue, time, random

input = lambda: sys.stdin.readline().rstrip()


def I():
    return input()


def IS():
    return input().split()


def II():
    return int(input())


def IIS():
    return map(int, input().split())


def LIIS():
    return list(map(int, input().split()))


def Base_n_to_10(X, n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(X[-i]) * (n**(i - 1))
    return out  #int out


def Base_10_to_n(X, n):
    if (X // n):
        return Base_10_to_n(X // n, n) + str(X % n)
    return str(X % n)


INF = 10**18
MOD = 10**9 + 7
sys.setrecursionlimit(10**8)
##############################################################################
n, Q = IIS()
path = [[] for i in range(n)]
for i in range(n - 1):
    a, b = IIS()
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
used = [False for i in range(n)]
val = [0 for i in range(n)]
used[0] = True
q = collections.deque()
q.append((0, 0))
while len(q):
    v, c = q.popleft()
    for i in path[v]:
        if used[i]: continue
        used[v] = True
        val[i] = c + 1
        q.append((i, c + 1))
for i in range(Q):
    c, d = IIS()
    if (val[d - 1] - val[c - 1]) % 2:
        print("Road")
    else:
        print("Town")
