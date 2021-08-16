# #template# # # # # # # # # # # # # # # # # #
def iin():  #int
    return int(input())


def fin():  #float
    return float(input())


def xin(opt=False):  #map(opt->0-indexed)
    x = map(int, input().split())
    if opt:
        return map(lambda x: x - 1, x)
    return x


def lin(opt=False):  #list(opt->0-indexed)
    return list(xin(opt))


def qin(q):  #query or matrix
    return [lin() for i in range(q)]


def gin(h):  #grid
    return [list(input()) for i in range(h)]


def cin():  #char list
    return list(input())


def slin():  #string list
    return input().split()


def stin():  #string
    return input()


def llin():  #num+list
    return iin(), lin()


def xlin():  #xin()+lin()
    return xin(), lin()


def yn(b):
    print(["No", "Yes"][b])


def lpr(lis, chr=" "):
    print(chr.join(map(str, lis)))


def gpr(lis):
    for i in lis:
        lpr(i)


def mkm(n, m, num=0):
    return [[num] * m for i in range(n)]


def invpow(x, mod):
    return pow(x, mod - 2, mod)


def modd(a, b, mod):
    return (a * invpow(b, mod)) % mod


mod = 10**9 + 7
# # # # # # # # # # # # # # # # # # # # # # #
import sys

sys.setrecursionlimit(101000)
n, q = lin()
E = [[] for i in range(n)]
for i in range(n - 1):
    a, b = lin(1)
    E[a].append(b)
    E[b].append(a)
seen = [-1] * n
seen[0] = 0


def dfs(x):
    for i in E[x]:
        if seen[i] == -1:
            seen[i] = seen[x] ^ 1
            dfs(i)


dfs(0)
for i in range(q):
    c, d = lin(1)
    print(["Road", "Town"][seen[c] == seen[d]])
