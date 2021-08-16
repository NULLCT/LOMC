import heapq
import sys
import math
# import numpy as np
from heapq import heappush, heappop
import inspect
import itertools
import bisect
from collections import deque
from collections import Counter
from collections import defaultdict
from decimal import Decimal

sys.setrecursionlimit(10**7)
MOD1 = 10**9 + 7
MOD2 = 998244353
MOD = MOD2
INF = float('inf')
DYDX = [(1, 0), (0, 1), (-1, 0), (0, -1)]
input = sys.stdin.readline


def ii():
    return int(input())


def si():
    return str(input()[:-1])


def li():
    return list(input())


def mi():
    return map(int, input().split())


def lmi():
    return list(map(int, input().split()))


def folmi(n):
    return [list(map(int, input().split())) for _ in range(n)]


def foli(n):
    return [list(input()[:-1]) for _ in range(n)]


def foi(n):
    return [input()[:-1] for _ in range(n)]


def foii(n):
    return [int(input()[:-1]) for _ in range(n)]


def lcm(a, b):
    return a // math.gcd(a, b) * b


def cnt_digits(a):
    return len(str(a))


###############################################################################

###############################################################################


def p(x):
    print(x)


def pmat(mat):
    for i in mat:
        print(i)


def dmat(mat):
    for i in mat:
        print(i, file=sys.stderr)


def dd(a, b=None, c=None, d=None):
    frame = inspect.currentframe()
    stack = inspect.getouterframes(frame)
    varnames = stack[1].code_context[0].split('(')[1].split(')')[0].split(",")
    outputs = []
    for i in range(len(varnames)):
        outputs.append("|")
        outputs.append(varnames[i])
        outputs.append("=")
        if i == 0:
            outputs.append(a)
        elif i == 1:
            outputs.append(b)
        elif i == 2:
            outputs.append(c)
        elif i == 3:
            outputs.append(d)
        if i == len(varnames) - 1:
            outputs.append("|")
    print(*outputs, file=sys.stderr)


def pow(x, n, mod):
    ans = 1
    while n > 0:
        if n % 2 != 0:
            ans *= x % mod
        x = x * x % mod
        n = n // 2
    return ans


def nck(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    return x * pow(y, mod - 2, mod) % mod


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def primes(x):
    if x < 2:
        return []
    primes = [i for i in range(x)]
    primes[1] = 0
    for prime in primes:
        if prime > math.sqrt(x):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, x, prime):
            primes[non_prime] = 0
    return [prime for prime in primes if prime != 0]


def prime_numbers(n):
    if n < 2:
        return []
    m = (n + 1) // 2
    p = [1] * m
    for i in range(1, int((n**0.5 - 1) / 2) + 1):
        if p[i]:
            p[2 * i * (i + 1):: 2 * i + 1] = [0] * \
                (((m - 1) - 2 * i * (i + 1)) // (2 * i + 1) + 1)
    return {2} | {2 * i + 1 for i in range(1, m) if p[i]}


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0:
            return False
        prime += step
        step = 6 - step
    return True


def prime_factorize_count(n):
    return Counter(prime_factorize(n))


class dsu:
    __slots__ = ["n", "parent_or_size"]

    def __init__(self, n):
        self.n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if self.parent_or_size[y] < self.parent_or_size[x]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        path = []
        while self.parent_or_size[a] >= 0:
            path.append(a)
            a = self.parent_or_size[a]
        for child in path:
            self.parent_or_size[child] = a
        return a

    def size(self, a):
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [g for g in result if g]


# def dijkstra(s, n):
#     dist = [INF] * (n + 1)
#     hq = [(0, s)]
#     dist[s] = 0
#     seen = [False] * (n + 1)
#     while hq:
#         v = heappop(hq)[1]
#         seen[v] = True
#         for to, cost in a[v]:
#             if seen[to] == False and dist[v] + cost < dist[to]:
#                 dist[to] = dist[v] + cost
#                 heappush(hq, (dist[to], to))
#     return dist

# nck modp
# MAX = 200010
# MOD = MOD1
# fac = [0] * MAX
# finv = [0] * MAX
# inv = [0] * MAX

# def cominit():
#     for i in range(2):
#         fac[i] = 1
#         finv[i] = 1
#     inv[1] = 1
#     for i in range(2, MAX):
#         fac[i] = fac[i - 1] * i % MOD
#         inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
#         finv[i] = finv[i - 1] * inv[i] % MOD

# def com(n, k):
#     return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (ModInt(self.x + other.x)
                if isinstance(other, ModInt) else ModInt(self.x + other))

    def __sub__(self, other):
        return (ModInt(self.x - other.x)
                if isinstance(other, ModInt) else ModInt(self.x - other))

    def __mul__(self, other):
        return (ModInt(self.x * other.x)
                if isinstance(other, ModInt) else ModInt(self.x * other))

    def __truediv__(self, other):
        return (ModInt(self.x * pow(other.x, MOD - 2, MOD)) if isinstance(
            other, ModInt) else ModInt(self.x * pow(other, MOD - 2, MOD)))

    def __pow__(self, other):
        return (ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt)
                else ModInt(pow(self.x, other, MOD)))

    __radd__ = __add__

    def __rsub__(self, other):
        return (ModInt(other.x - self.x)
                if isinstance(other, ModInt) else ModInt(other - self.x))

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (ModInt(other.x * pow(self.x, MOD - 2, MOD)) if isinstance(
            other, ModInt) else ModInt(other * pow(self.x, MOD - 2, MOD)))

    def __rpow__(self, other):
        return (ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt)
                else ModInt(pow(other, self.x, MOD)))


###############################################################################
#
###############################################################################
n, q = mi()
edge = [[] for _ in range(n)]
dep = [0] * n

for i in range(n - 1):
    a, b = mi()
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


def dfs(x, last=-1):
    for to in edge[x]:
        if to == last:
            continue
        dep[to] = dep[x] + 1
        dfs(to, x)


dfs(0)

for _ in range(q):
    c, d = mi()
    c -= 1
    d -= 1
    if dep[c] & 1 == dep[d] & 1:
        p("Town")
    else:
        p("Road")
