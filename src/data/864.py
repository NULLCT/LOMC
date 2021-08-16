import bisect, collections, copy, heapq, itertools, math, string, sys, queue, time, random

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)


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
n, q = IIS()
path = [[] for i in range(n)]
for i in range(n - 1):
    a, b = IIS()
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
used = [False for i in range(n)]
st = set()
li = [0 for i in range(n)]


def EulerTour(n, X, i0):
    done = [0] * n
    Q = [~i0, i0]  # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0:  # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                Q.append(~a)  # 帰りがけの処理をスタックに追加
                Q.append(a)  # 行きがけの処理をスタックに追加

        else:  # 帰りがけの処理
            ET.append(~i)

    return ET


li2 = [-1 for i in range(n)]
li3 = [0 for i in range(n)]
li = EulerTour(n, path, 0)
for i in range(n * 2):
    if li2[li[i]] == -1:
        li2[li[i]] = i
    else:
        li3[li[i]] = i
for i in range(q):
    c, d = IIS()
    if min(abs(li3[c - 1] - li2[d - 1]), abs(li2[c - 1] - li3[d - 1])) % 2:
        print("Town")
    else:
        print("Road")
