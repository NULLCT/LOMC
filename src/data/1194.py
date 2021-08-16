import sys, os, io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
import math

alphabets = list('abcdefghijklmnopqrstuvwxyz')

#for deep recursion__________________________________________-
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    c = dict(Counter(l))
    return list(set(l))
    # return c


def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p
    return res


#____________________GetPrimeFactors in log(n)________________________________________
def sieveForSmallestPrimeFactor():
    MAXN = 100001
    spf = [0 for i in range(MAXN)]
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i
    return spf


def getPrimeFactorizationLOGN(x):
    spf = sieveForSmallestPrimeFactor()
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
    return ret


#____________________________________________________________


def SieveOfEratosthenes(n):
    #time complexity = nlog(log(n))
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def si():
    return input()


def divideCeil(n, x):
    if (n % x == 0):
        return n // x
    return n // x + 1


def ii():
    return int(input())


def li():
    return list(map(int, input().split()))


#__________________________TEMPLATE__________________OVER_______________________________________________________

if (os.path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append(
                [func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin],
                         self._data[depth][end - (1 << depth)])


class LCA:
    def __init__(self, root, graph):
        self.time = [-1] * len(graph)
        self.path = [-1] * len(graph)
        P = [-1] * len(graph)
        t = -1
        dfs = [root]
        while dfs:
            node = dfs.pop()
            self.path[t] = P[node]
            self.time[node] = t = t + 1
            for nei in graph[node]:
                if self.time[nei] == -1:
                    P[nei] = node
                    dfs.append(nei)
        self.rmq = RangeQuery(self.time[node] for node in self.path)

    def __call__(self, a, b):
        if a == b:
            return a
        a = self.time[a]
        b = self.time[b]
        if a > b:
            a, b = b, a
        return self.path[self.rmq.query(a, b)]


n, qq = li()
graph = [[] for i in range(n)]
for i in range(n - 1):
    a, b = li()
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

lca = LCA(0, graph)

dis = [0] * n
q = [0]
vis = [False] * n
vis[0] = True
while q:
    node = q.pop(0)
    for kid in graph[node]:
        if vis[kid] == False:
            vis[kid] = True
            dis[kid] = 1 + dis[node]
            q.append(kid)
for i in range(qq):
    a, b = li()
    a -= 1
    b -= 1
    commonNode = lca.__call__(a, b)
    d = dis[a] + dis[b] - 2 * dis[commonNode]
    # print(d)
    if d % 2 == 1:
        print('Road')
    else:
        print("Town")
