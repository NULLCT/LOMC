""" convenient functions
# for i, a in enumerate(iterable)
# q, mod = divmod(a, b)
# divmod(x, y) returns the tuple (x//y, x%y)
# Higher-order function: reduce(operator.mul, xyz_count, 1)
# manage median(s) using two heapq https://atcoder.jp/contests/abc127/tasks/abc127_f
"""
"""convenient decorator
# @functools.lru_cache():
# to facilitate use of recursive function
    # ex:
    # from functools import lru_cache
    # import sys
    # sys.setrecursionlimit(10**9)
    # @lru_cache(maxsize=None)
    # def fib(n):
    #     if n < 2:
    #         return n
    #     return fib(n-1) + fib(n-2)
    # print(fib(1000))
"""

import sys

sys.setrecursionlimit(10**9)
import typing
from typing import Deque, List, Tuple, Any, Callable

from itertools import accumulate, combinations, permutations, product, combinations_with_replacement  # https://docs.python.org/ja/3/library/itertools.html
# accumulate() returns iterator! to get list: list(accumulate())
from math import factorial, ceil, floor, sqrt
from math import degrees, radians, tan, atan, atan2, cos, acos, sin, asin, pi
# radians(180) が180°を意味します。sin180°はsin(radians(180))と書けばOK。誤差があるので、完全一致必要な場合は注意。
# degrees(atan(1)) => 45.0

# class Vec2D():
#     """2つの2次元ベクトルから間の角度を回転方向付きで求める(-pi < theta <= pi)
#     # 未完成
#     calc_thetaで求めた値はcos()などの引数として使用できる。
#     ref: http://www5d.biglobe.ne.jp/~noocyte/Programming/Geometry/RotationDirection.html#GetAngle
#     ref: https://atcoder.jp/contests/abc207/tasks/abc207_d
#     """
#     def __init__(self, va: List[int], vb: List[int]) -> None:
#         self.va = va
#         self.vb = vb
#         self.inner_product = self.inner_product_2D(self.va, self.vb)
#         self.cross_product = self.cross_product_2D(self.va, self.vb)
#         self.theta = self.calc_theta(self.cross_product, self.inner_product)

#     def inner_product_2D(self, va: List[int], vb: List[int]) -> int:
#         return sum([a*b for a, b in zip(va, vb)])

#     def cross_product_2D(self, va: List[int], vb: List[int]) -> int:
#         return va[0]*vb[1] - va[1]*vb[0]

#     def calc_theta(self, cross_product: int, inner_product: int) -> float:
#         return atan2(cross_product, inner_product)

# optimize # for python (not pypy)
# from scipy.optimize import fmin
# https://atcoder.jp/contests/abc151/tasks/abc151_f
# ex:
# def calc(k):
#     i, j = k
#     ans = 0
#     for x, y in XY:
#         ans = max(ans, (x-i)**2+(y-j)**2)
#     return ans
# x, y = fmin(calc, [500, 500], disp=0)


def sum_xor(A: List, max_digit: int = 61, MOD: int = 10**9 + 7):
    # https://atcoder.jp/contests/abc147/tasks/abc147_d
    # count_each_digit
    L: List[int] = [0] * max_digit
    for a in A:
        tmp = a
        current_digit = 0
        while tmp:
            tmp, residual = divmod(tmp, 2)
            if residual:
                L[current_digit] += 1
            current_digit += 1

    ans: int = 0
    tmp: int = 1
    for i in range(max_digit):
        ans += (len(A) - L[i]) * L[i] * tmp
        ans %= MOD
        tmp *= 2
        tmp %= MOD
    return ans


def factorize(n):
    """return the factors of the Arg and count of each factor
    
    Args:
        n (long): number to be resolved into factors
    
    Returns:
        list of tuples: factorize(220) returns [(2, 2), (5, 1), (11, 1)]
    """
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def combinations_count(n, r):
    """Return the number of selecting r pieces of items from n kinds of items.
    
    Args:
        n (long): number
        r (long): number
    
    Raises:
        Exception: not defined when n or r is negative
    
    Returns:
        long: number
    """
    # TODO: How should I do when n - r is negative?
    if n < 0 or r < 0:
        raise Exception(
            'combinations_count(n, r) not defined when n or r is negative')
    if n - r < r: r = n - r
    if r < 0: return 0
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


def combinations_with_replacement_count(n, r):
    """Return the number of selecting r pieces of items from n kinds of items allowing individual elements to be repeated more than once.
    
    Args:
        n (long): number
        r (long): number
    
    Raises:
        Exception: not defined when n or r is negative
    
    Returns:
        long: number
    """
    if n < 0 or r < 0:
        raise Exception(
            'combinations_with_replacement_count(n, r) not defined when n or r is negative'
        )
    elif n == 0:
        return 1
    else:
        return combinations_count(n + r - 1, r)


def permutations_count(n, r, MOD=None):
    ans = 1
    if MOD:
        for i in range(r):
            ans = (ans * (n - i)) % MOD
    else:
        for i in range(r):
            ans = (ans * (n - i))
    return ans


from copy import deepcopy, copy  # https://docs.python.org/ja/3/library/copy.html
import operator
# from operator import add, mul
from operator import itemgetter  #sort
# ex1: List.sort(key=itemgetter(1))
# ex2: sorted(tuples, key=itemgetter(1,2))
# ex3: ABC.sort(key=lambda x: x[0]+x[1]) # sort by a+b <= itemgetter is not used
from functools import partial, reduce, lru_cache


# ************ DP ************
def chmin(dp, i, x):
    """chmin; same as:
    dp[i] = min(dp[i], x)
    ref: https://twitter.com/cs_c_r_5/status/1266610488210681857
    Args:
        dp (list): one dimensional list
        i (int): index of dp
        x (int): value to be compared with

    Returns:
        bool: True if update is done
    
    ex:
        # one dimensional dp
        chmin(dp,i,x)
        
        # two dimensional dp
        chmin(dp[i],j,x)
    """
    if x < dp[i]:
        dp[i] = x
        return True
    return False


def chmax(dp, i, x):
    """chmax; same as:
    dp[i] = max(dp[i], x)
    ref: https://twitter.com/cs_c_r_5/status/1266610488210681857
    Args:
        dp (list): one dimensional list
        i (int): index of dp
        x (int): value to be compared with

    Returns:
        bool: True if update is done
    
    ex:
        # one dimensional dp
        chmax(dp,i,x)
        
        # two dimensional dp
        chmax(dp[i],j,x)
    """
    if x > dp[i]:
        dp[i] = x
        return True
    return False


# ************ bit演算 ************
# bitcount (population count; popcount)
def bit_count(x):
    """count number of bit
    # ref: https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
    Args:
        x (int): number. Advice: use int('10110', 2) if input is '10110'
    Returns:
        int: bit summation
    """
    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)
    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    # bin(0x333) => 0b1100110011
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007f


def bit_last(x):
    """
    Get the last digit where 1 stands (0-indexed)
    x.bit_length()と同じ。
    ref: https://www.slideshare.net/KMC_JP/slide-www

    Args:
        x (int): bit

    Returns:
        int: last digit
    
    >>> bit_last(1)
    0
    >>> bit_last(4)
    2
    >>> bit_last(6)
    1
    >>> bit_last(0b1011000)
    3
    """
    return (x & -x).bit_length() - 1


def bit_first(x):
    """Get the first digit where 1 stands(0-indexed)

    Args:
        x (int): bit

    Returns:
        int: first digit
    >>> bit_first(1)
    0
    >>> bit_first(4)
    2
    >>> bit_first(6)
    2
    >>> bit_first(0b1011000)
    6
    """
    return x.bit_length() - 1


atoz = list('abcdefghijklmnopqrstuvwxyz')  # 26
AtoZ = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # 26
HEXADECIMAL = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}
ALPHAtoNUM = lambda c: ord(c) - ord('A') + 1
alphatonum = lambda c: ord(c) - ord('a') + 1
atoA = {a: A for a, A in zip(atoz, AtoZ)}
Atoa = {A: a for a, A in zip(atoz, AtoZ)}
YesNo = lambda condition, Yes='Yes', No='No': print(
    Yes) if condition else print(No)
# ************ Math ************
# greatest common divisor
from math import gcd
# from fractions import gcd
# def gcd(a,b):
#     # from fractions import gcd # Deprecated since version 3.5: Use math.gcd() instead.
#     # => 最近の環境でfractions.gcdを使うとTLEする。
#     # aまたはbが0の場合もう一方を返すようにすると良いかも。gcdの単位元を0とするケースがあるため。
#     if a<b:
#         a, b = b, a
#     while a%b !=0 :
#         a, b = b, a%b
#     return b

# def gcd(p,q):
#     while q != 0:
#         r = p % q
#         p = q
#         q = r
#     return p


def gcds(numbers):
    return reduce(gcd, numbers)


# least common multiple
def lcm(x, y):
    return (x * y) // gcd(x, y)


def lcms(numbers):
    return reduce(lcm, numbers, 1)


# 約数列挙 約数
def make_divisors(n, reversed=False):
    """create list of divisors O(root(N))
    
    Args:
        number (int): number from which list of divisors is created
        reversed (bool, optional): ascending order if False. Defaults to False.
    
    Returns:
        list: list of divisors
    """
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors), reverse=reversed)


# Eratosthenesの篩により、整数end未満の素数を列挙する 素数 "素数List"と"is_prime"を返す。
def sieve_of_eratosthenes(end, typecode="L"):
    """get primes list and is_prime list 
    # len(sieve_of_eratosthenes(10**7)) => 664579; 514ms in pypy
    # len(sieve_of_eratosthenes(10**6)) => 78498; 134ms in pypy
 
    # https://hamukichi.hatenablog.jp/entry/2016/02/17/215948#Eratosthenes%E3%81%AE%E7%AF%A9%E3%81%A8%E5%8C%BA%E9%96%93%E7%AF%A9

    Args:
        end (int): maximum number to be checked
        typecode (str, optional): I don't know.. Defaults to "L".

    Returns:
        array, array: primes, is_prime
    """
    import array
    import textwrap
    assert end > 1
    # 整数iが素数であるかをis_prime[i]が示す
    # 最初はすべてTrueで初期化しておく
    # 最終的にprimesではなくこれを返してもよい
    is_prime = array.array("B", (True for i in range(end)))
    # 0, 1はいずれも素数ではない
    is_prime[0] = False
    is_prime[1] = False
    # 素数を格納する配列
    primes = array.array(typecode)
    # 篩う
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False  # 素数ではないため除外する
    return primes, is_prime


# 因数分解 因数
class PrimeFactorization:
    '''初期化にO(NloglogN), 因数分解クエリをO(log(k)), 素数判定クエリをO(1)で行う
    >>> pf = PrimeFactorization(100)
    >>> pf.query(100)
    ((2, 2), (5, 2))
    >>> pf.is_prime(97)
    True
    >>> pf.is_prime(99)
    False
    >>> pf.divisors(100)
    [1, 2, 4, 5, 10, 20, 25, 50, 100]
    '''

    # 自分で実装した。
    # https://atcoder.jp/contests/abc177/editorial/82
    # 高速素因数分解
    # 問題： A 以下の数が N 個与えられる。全て素因数分解せよ。
    # 前計算としてエラトステネスの篩を行い、「その数をふるい落とした素数」を配列 D に記録します。
    # 例えば D[4]=D[6]=2,D[35]=5 です。x が素数のときは D[x]=x としておきます。この配列はエラトステネスの篩と同様 O(AloglogA) で構築できます。
    # D[x] は x を割り切る最小の素数なので、この配列 D を利用すると素因数分解を行うときに「試し割り」をする必要がなくなり(D[x]で割ればよい)、1つの数の素因数分解が素因数の個数である O(logA) でできるようになります。
    def __init__(self, Num=10**6):
        # from collections import defaultdict
        from math import floor
        self.Num = Num
        self.D = [-1] * (Num + 1)
        for i in range(2, Num + 1):
            if self.D[i] != -1:
                continue
            self.D[i] = i
            for j in range(1, floor(Num / i) + 1):
                if self.D[j * i] != -1:
                    continue
                else:
                    self.D[j * i] = i

    def divisors(self, k):
        """
        ex:
        >>> pf = PrimeFactorization(300)
        >>> pf.divisors(300)
        [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 25, 30, 50, 60, 75, 100, 150, 300]
        """
        if k == 1:
            return [1]
        return sorted(
            reduce(lambda x, y: x * y, i)
            for i in product(*[[pow(a, bb) for bb in range(b + 1)]
                               for a, b in self.query(k)]))

    def query(self, k):
        """
        ex:
        >>> pf = PrimeFactorization(100)
        >>> pf.query(100)
        ((2, 2), (5, 2))
        """
        from collections import defaultdict
        ans = defaultdict(int)
        tmp = k
        while self.D[tmp] != -1:
            div = self.D[tmp]
            ans[div] += 1
            tmp = tmp // div
        return tuple(ans.items())

    def is_prime(self, k):
        return k == self.D[k]


INF = 10**18
modpow = lambda a, n, p: pow(a, n, p)  # Recursive function in python is slow!


def modinv_Fermat(a, p):
    # evaluate reciprocal using Fermat's little theorem:
    # a**(p-1) is identical to 1 (mod p) when a and p is coprime
    return modpow(a, p - 2, p)


def modinv(a, p):
    # inverse_element 逆元
    # 多分 O(log N)
    # https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a
    b, u, v = p, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= p
    if u < 0:
        u += p
    return u


def modinv_list(n, p):
    if n <= 1:
        return [0, 1][:n + 1]
    else:
        inv_t = [0, 1]
        for i in range(2, n + 1):
            inv_t += [inv_t[p % i] * (p - int(p / i)) % p]
        return inv_t


# factorial: 階乗
def modfactorial_list(n, p):
    if n == 0:
        return [1]
    else:
        l = [0] * (n + 1)
        tmp = 1
        for i in range(1, n + 1):
            tmp = tmp * i % p
            l[i] = tmp
        return l


def modcomb(n, k, p, fac_list=None):
    if not fac_list:
        fac_list = []
    # fac_list = modfactorial_list(100)
    # print(modcomb(100, 5, modfactorial_list(100)))
    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    if len(fac_list) <= n:
        a = factorial(n) % p
        b = factorial(k) % p
        c = factorial(n - k) % p
    else:
        a = fac_list[n]
        b = fac_list[k]
        c = fac_list[n - k]
    return (a * modpow(b, p - 2, p) * modpow(c, p - 2, p)) % p


class ModComb:
    """MODのcombinationsや整数の逆元, 階乗, 階乗の逆元を求める。準備にO(NlogN)?
    ref: https://atcoder.jp/contests/abc167/submissions/13041012

    使い方:
        fact: 階乗(O(1))
        fact_inv: 階乗の逆元(O(1))
        comb: combinations(O(1))
        inv: 階乗(O(1))

    ex:
        comb = ModComb(n, mod)
        print(comb.comb(n, k))
    """
    def __init__(self, n, MOD):
        self.n = n
        self.MOD = MOD
        self.fact = self.make_fact(n)
        self.fact_inv = self.make_fact_inv(n)

    def make_fact(self, n):  #0~nの階乗を求める
        res = [1] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i - 1] * i % self.MOD
        return res

    def make_fact_inv(self, n):  #0~nの階乗のMODに関する逆元を求める
        fact_inv = [1] * (n + 1)
        fact_inv[n] = self.modinv(self.fact[n])  # 拡張ユークリッドの互除法にした
        # fact_inv[n] = pow(self.fact[n], self.MOD-2, self.MOD)#フェルマーの小定理
        for i in range(n, 0, -1):
            fact_inv[i - 1] = fact_inv[i] * i % self.MOD
        return fact_inv

    def comb(self, m, k):
        if m < k: return 0
        if m < 0 or k < 0: return 0  # 本当か？
        return self.fact[m] * self.fact_inv[k] * self.fact_inv[m -
                                                               k] % self.MOD

    def modinv(self, a):
        # inverse_element 逆元
        # https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a
        p = self.MOD
        b, u, v = p, 1, 0
        while b:
            t = a // b
            a -= t * b
            a, b = b, a
            u -= t * v
            u, v = v, u
        u %= p
        if u < 0:
            u += p
        return u

    def inv(self, n):
        return (self.fact_inv[n] * self.fact[n - 1]) % self.MOD


def modadd(a, b, p):
    return (a + b) % p


def modsub(a, b, p):
    return (a - b) % p


def modmul(a, b, p):
    return ((a % p) * (b % p)) % p


def moddiv_Fermat(a, b, p):
    # 法 p が素数でないと使えない
    return modmul(a, modpow(b, p - 2, p), p)


def moddiv(a, b, p):
    # https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a
    # 法 pp が素数でなくても逆元存在条件を満たせば使える
    return modmul(a, modinv(b, p), p)


MOD_MODINT = 10**9 + 7


# MOD_MODINT = 998244353
class ModInt(int):
    """ref: https://atcoder.jp/contests/abc147/submissions/9330230?lang=ja
    Caution: MOD_MODINTを直して使う必要がある。
    TODO: __eq__系が欠けていたので追加した。もう少し機能完備したものを誰かが作っていると思う。探すか作りましょう。
    memo: intを継承させた。これによりlistのslice材料として使えるようになった。（そもそもそういう数値はmodint型にする必要なさそうだが） ref: https://twitter.com/maspy_stars/status/1218419292187889664/photo/1
    """
    def __init__(self, x):
        self.x = x % MOD_MODINT

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
        return (ModInt(self.x * pow(other.x, MOD_MODINT - 2, MOD_MODINT))
                if isinstance(other, ModInt) else ModInt(
                    self.x * pow(other, MOD_MODINT - 2, MOD_MODINT)))

    __floordiv__ = __truediv__  # //

    def __eq__(self, other):
        return (self.x == other.x
                if isinstance(other, ModInt) else self.x == other)

    def __ne__(self, other):
        return (self.x != other.x
                if isinstance(other, ModInt) else self.x != other)

    def __lt__(self, other):
        return (self.x < other.x
                if isinstance(other, ModInt) else self.x < other)

    def __gt__(self, other):
        return (self.x > other.x
                if isinstance(other, ModInt) else self.x > other)

    def __le__(self, other):
        return (self.x <= other.x
                if isinstance(other, ModInt) else self.x <= other)

    def __ge__(self, other):
        return (self.x >= other.x
                if isinstance(other, ModInt) else self.x >= other)

    def __pow__(self, other):
        return (ModInt(pow(self.x, other.x, MOD_MODINT)) if isinstance(
            other, ModInt) else ModInt(pow(self.x, other, MOD_MODINT)))

    __radd__ = __add__

    def __rsub__(self, other):
        return (ModInt(other.x - self.x)
                if isinstance(other, ModInt) else ModInt(other - self.x))

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (ModInt(other.x * pow(self.x, MOD_MODINT - 2, MOD_MODINT))
                if isinstance(other, ModInt) else ModInt(
                    other * pow(self.x, MOD_MODINT - 2, MOD_MODINT)))

    def __rpow__(self, other):
        return (ModInt(pow(other.x, self.x, MOD_MODINT)) if isinstance(
            other, ModInt) else ModInt(pow(other, self.x, MOD_MODINT)))

    def __iadd__(self, other):
        self.x += other.x if isinstance(other, ModInt) else other
        self.x %= MOD_MODINT
        return self

    def __isub__(self, other):
        self.x += ModInt(MOD_MODINT - other.x) if isinstance(
            other, ModInt) else ModInt(MOD_MODINT - other)
        return self

    def __imul__(self, other):
        self.x *= other.x if isinstance(other, ModInt) else other
        self.x %= MOD_MODINT
        return self

    def factorical(self, n):
        tmp = ModInt(1)
        for i in range(n):
            tmp *= (i + 1)
        return tmp

    #m:int MOD_MODINT
    def modinv(self, a, m=MOD_MODINT):
        b = m
        u = 1
        v = 0
        while (b):
            t = a // b
            a -= t * b
            a, b = b, a
            u -= t * v
            u, v = v, u
        return ModInt(u)

    def comb(self, n, r):
        n = int(n)
        r = int(r)
        if r > n or n < 0 or r < 0:
            return 0
        m = n + 1
        nterms = min(r, n - r)
        numerator = ModInt(1)
        denominator = ModInt(1)
        for j in range(1, nterms + 1):
            numerator *= m - j
            denominator *= j
        return numerator * self.modinv(denominator.x)


class Math():
    """
    ref: https://github.com/shakayami/ACL-for-python/blob/master/math.py
    ref: https://qiita.com/R_olldIce/items/3e2c80baa6d5e6f3abe9
    """
    @classmethod
    def inv_gcd(cls, a, b):
        a = a % b
        if a == 0:
            return (b, 0)
        s = b
        t = a
        m0 = 0
        m1 = 1
        while (t):
            u = s // t
            s -= t * u
            m0 -= m1 * u
            s, t = t, s
            m0, m1 = m1, m0
        if m0 < 0:
            m0 += b // s
        return (s, m0)

    @classmethod
    def inv_mod(cls, x, m):
        assert 1 <= m
        z = cls.inv_gcd(x, m)
        assert z[0] == 1
        return z[1]

    @classmethod
    def crt(cls, r: typing.List[int], m: typing.List[int]):
        """chinese remainder theorem
        ref: https://qiita.com/R_olldIce/items/3e2c80baa6d5e6f3abe9
        ref: https://www.creativ.xyz/ect-gcd-crt-garner-927/
        ref: https://qiita.com/drken/items/ae02240cd1f8edfc86fd
        TODO: アルゴリズムの理解

        Args:
            r (list): r from [x = r0 mod m0, r1 mod m1, r2 mod m2..]
            m (list): m from [x = r0 mod m0, r1 mod m1, r2 mod m2..]

        Returns:
            tuple: (r, m) of x = r mod m if answer exists else (0, 0)
        """
        assert len(r) == len(m)
        n = len(r)
        r0 = 0
        m0 = 1
        for i in range(n):
            assert 1 <= m[i]
            r1 = r[i] % m[i]
            m1 = m[i]
            if m0 < m1:
                r0, r1 = r1, r0
                m0, m1 = m1, m0
            if (m0 % m1 == 0):
                if (r0 % m1 != r1):
                    return (0, 0)
                continue
            g, im = cls.inv_gcd(m0, m1)
            u1 = m1 // g
            if ((r1 - r0) % g):
                return (0, 0)
            x = (r1 - r0) // g % u1 * im % u1
            r0 += x * m0
            m0 *= u1
            if r0 < 0:
                r0 += m0
        return (r0, m0)

    @classmethod
    def floor_sum(cls, n: int, m: int, a: int, b: int):
        """ref: https://atcoder.jp/contests/practice2/editorial/579
        TODO: アルゴリズムの理解

        Args:
            n (int): [description]
            m (int): [description]
            a (int): [description]
            b (int): [description]

        Returns:
            int: Sum_(i=0~n-1)floor((a*i+b)/m)
            O(log a + log m)
        """
        ans = 0
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y_max = (a * n + b) // m
        x_max = (y_max * m - b)
        if y_max == 0:
            return ans
        ans += (n - (x_max + a - 1) // a) * y_max
        ans += cls.floor_sum(y_max, a, m, (a - x_max % a) % a)
        return ans


def extGCD(a: int, b: int):
    """answer pair (x, y) of equation ax + by = gcd(a, b)

    Args:
        a (int): [description]
        b (int): [description]

    Returns:
        typle: answer pair (x, y)
    """
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y


# get [Sigma_j=0~i(A_j*B_i-j) for i in range(N)]
class Convolution:
    """高速フーリエ変換 
    # 使用例
    
    # 以下の2行はグローバルに書いている。これが早いみたい。
    MOD_COMV = 998244353 # 1007681537 でも良いらしい
    conv=Convolution()
    
    # main関数内
    A, B: List[int]
    print(*conv.convolution(A,B))

    # この実装：https://atcoder.jp/contests/atc001/submissions/17104531
    # 他の実装や解説
    # https://github.com/shakayami/ACL-for-python/wiki
    # https://atcoder.jp/contests/atc001/submissions/17104531
    # 問題
    # https://atcoder.jp/contests/atc001/tasks/fft_c
    # https://atcoder.jp/contests/practice2/submissions/16789717

    # 998244353=119 * 2^23 + 1と書けるため、この素数はFFTに適しています。 2で23回割り切れるため、この場合はAとBの畳み込みを計算するときに、リストの大きさがlen(A)+len(B)-1<=2^23以内ならば畳み込みを正常に計算することが出来ます。
    """
    def __init__(self):
        # self.MOD_COMV = MOD_COMV # 遅くなる
        self.g = self.primitive_root(MOD_COMV)
        self.first_butterfly = True
        self.first_butterfly_inv = True
        self.sum_e = [0] * 30
        self.sum_ie = [0] * 30

    # 原始根の取得
    def primitive_root(self, m: int):
        if (m == 2):
            return 1
        if (m == 167772161):
            return 3
        if (m == 469762049):
            return 3
        if (m == 754974721):
            return 11
        if (m == 998244353):
            return 3
        divs = [0] * 20
        divs[0] = 2
        cnt = 1
        x = (m - 1) // 2
        while (x % 2 == 0):
            x //= 2
        for i in range(3, x + 1, 2):
            if (i**2 > x):
                break
            if (x % i == 0):
                divs[cnt] = i
                cnt += 1
                while (x % i == 0):
                    x //= i
        if (x > 1):
            divs[cnt] = x
            cnt += 1
        g = 2
        while (True):
            ok = True
            for i in range(cnt):
                if (pow(g, (m - 1) // divs[i], m) == 1):
                    ok = False
                    break
            if (ok):
                return g
            g += 1

        print('error')
        return 0

    def butterfly(self, a: list):
        # MOD_COMV = self.MOD_COMV
        n = len(a)
        h = (n - 1).bit_length()
        if (self.first_butterfly):
            self.first_butterfly = False
            es = [0] * 30
            ies = [0] * 30
            mod_m = MOD_COMV - 1
            cnt2 = (mod_m & -mod_m).bit_length() - 1
            e = pow(self.g, mod_m >> cnt2, MOD_COMV)
            ie = pow(e, MOD_COMV - 2, MOD_COMV)
            for i in range(cnt2 - 2, -1, -1):
                es[i] = e
                ies[i] = ie
                e *= e
                e %= MOD_COMV
                ie *= ie
                ie %= MOD_COMV
            now = 1
            for i in range(cnt2 - 1):
                self.sum_e[i] = (es[i] * now) % MOD_COMV
                now *= ies[i]
                now %= MOD_COMV
        for ph in range(1, h + 1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            now = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * now
                    a[i + offset] = (l + r) % MOD_COMV
                    a[i + offset + p] = (l - r) % MOD_COMV
                now *= self.sum_e[(~s & -~s).bit_length() - 1]
                now %= MOD_COMV

    def butterfly_inv(self, a: list):
        # MOD_COMV = self.MOD_COMV
        n = len(a)
        h = (n - 1).bit_length()
        if (self.first_butterfly_inv):
            self.first_butterfly_inv = False
            es = [0] * 30
            ies = [0] * 30
            mod_m = MOD_COMV - 1
            cnt2 = (mod_m & -mod_m).bit_length() - 1
            e = pow(self.g, mod_m >> cnt2, MOD_COMV)
            ie = pow(e, MOD_COMV - 2, MOD_COMV)
            for i in range(cnt2 - 2, -1, -1):
                es[i] = e
                ies[i] = ie
                e *= e
                e %= MOD_COMV
                ie *= ie
                ie %= MOD_COMV
            now = 1
            for i in range(cnt2 - 1):
                self.sum_ie[i] = (ies[i] * now) % MOD_COMV
                now *= es[i]
                now %= MOD_COMV
        for ph in range(h, 0, -1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            inow = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l + r) % MOD_COMV
                    a[i + offset + p] = ((l - r) * inow) % MOD_COMV
                inow *= self.sum_ie[(~s & -~s).bit_length() - 1]
                inow %= MOD_COMV

    def convolution(self, a: list, b: list):
        # MOD_COMV = self.MOD_COMV
        n = len(a)
        m = len(b)
        if (n == 0) | (m == 0):
            return []
        if (min(n, m) <= 60):
            if (n < m):
                a, b = b, a
                n, m = m, n
            ans = [0] * (n + m - 1)
            for i in range(n):
                for j in range(m):
                    ans[i + j] += a[i] * b[j]
                    ans[i + j] %= MOD_COMV
            return ans

        z = 1 << (n + m - 2).bit_length()
        a += [0] * (z - n)
        b += [0] * (z - m)
        self.butterfly(a)
        self.butterfly(b)
        for i in range(z):
            a[i] *= b[i]
            a[i] %= MOD_COMV
        self.butterfly_inv(a)
        a = a[:(n + m - 1)]
        iz = pow(z, MOD_COMV - 2, MOD_COMV)
        for i in range(n + m - 1):
            a[i] *= iz
            a[i] %= MOD_COMV
        return a

    def convolution_ll(self, a: list, b: list):
        from math import gcd
        global MOD_COMV
        n = len(a)
        m = len(b)
        if (n == 0) | (m == 0):
            return []

        MOD1 = 754974721  # 2^24
        MOD2 = 167772161  # 2^25
        MOD3 = 469762049  # 2^26
        M2M3 = MOD2 * MOD3
        M1M3 = MOD1 * MOD3
        M1M2 = MOD1 * MOD2
        M1M2M3 = MOD1 * MOD2 * MOD3

        i1 = gcd(M2M3, MOD1) * pow(M2M3 % MOD1, MOD1 - 2, MOD1) % MOD1
        i2 = gcd(M1M3, MOD2) * pow(M1M3 % MOD2, MOD2 - 2, MOD2) % MOD2
        i3 = gcd(M1M2, MOD3) * pow(M1M2 % MOD3, MOD3 - 2, MOD3) % MOD3

        MOD_COMV = MOD1
        A = a[::]
        B = b[::]
        self.__init__()
        c1 = self.convolution(A, B)
        MOD_COMV = MOD2
        # A = a[::]
        # B = b[::]
        self.__init__()
        c2 = self.convolution(A, B)
        MOD_COMV = MOD3
        # A = a[::]
        # B = b[::]
        self.__init__()
        c3 = self.convolution(A, B)

        c = [0] * (n + m - 1)
        for i in range(n + m - 1):
            x = 0
            x += (c1[i] * i1) % MOD1 * M2M3
            x += (c2[i] * i2) % MOD2 * M1M3
            x += (c3[i] * i3) % MOD3 * M1M2
            c[i] = x % M1M2M3

        return c


MOD_COMV = 998244353
conv = Convolution()


def ternary_search(f: Callable[[float], float], high: float,
                   low: float) -> float:
    # 三分探索の基本形
    # ref: https://juppy.hatenablog.com/entry/2019/04/11/ARC054_-B_%E3%83%A0%E3%83%BC%E3%82%A2%E3%81%AE%E6%B3%95%E5%89%87_-_%E4%B8%89%E5%88%86%E6%8E%A2%E7%B4%A2_Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder
    # ref: https://atcoder.jp/contests/arc122/tasks/arc122_b
    # ref: https://atcoder.jp/contests/arc122/submissions/23395538

    # N = r_int()
    # A = R()

    # high = INF
    # low = 0.00000001

    # def f(mid):
    #     cost = mid*N
    #     for a in A:
    #         cost -= min(a, 2*mid)
    #     return cost

    # high = ternary_search(f, high, low)
    # print(sum([high+a-min(a, 2*high) for a in A])/len(A))

    while high - low > 0.000000001 and (high / low) > 1.00000001:
        mid_left = high / 3 + low * 2 / 3
        mid_right = high * 2 / 3 + low / 3
        if f(mid_left) >= f(mid_right):
            low = mid_left
        else:
            high = mid_right
    return high


# ************ Data Structure ************
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict  # https://docs.python.org/ja/3/library/collections.html#collections.deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest  # https://docs.python.org/ja/3/library/heapq.html


class Heap:
    """
    heapqのwrap
    pop(), push(), pushpop()がある。
    ex:
    heap = Heap([])で初期化。
    while heap:
        s = heap.pop()
    """
    def __init__(self, L):
        self.heaplist = L
        heapify(self.heaplist)

    def __bool__(self):
        return bool(self.heaplist)

    def pop(self):
        return heappop(self.heaplist)

    def push(self, x):
        heappush(self.heaplist, x)

    def pushpop(self, x):
        return heappushpop(self.heaplist, x)


class HeapDict:
    """
    heap + erase item: O(logN) + item exists: O(1)
    https://tsubo.hatenablog.jp/entry/2020/06/15/124657

    pop(), push(), erace(), exist(), min, heaplist

    ex:
    heap = HeapDict([]) # initialize
    while heap:
        s = heap.pop()
    """
    def __init__(self, L=None):
        self.d = defaultdict(int)
        if L is None:
            self.heaplist = []
        else:
            self.heaplist = L
            heapify(self.heaplist)
            for l in L:
                self.d[l] += 1

    def __bool__(self):
        return bool(self.heaplist)

    def __contains__(self, v):
        return self.d[v]

    def push(self, x):
        heappush(self.heaplist, x)
        self.d[x] += 1

    def pop(self):
        """TODO: 追加したけど正しいですか？

        Returns:
            [type]: [description]
        """
        tmp = self.heaplist[0]
        self.erase(tmp)
        return tmp

    def erase(self, x):
        """erace and return True (if x not exist, return False)

        Args:
            x (int): value

        Returns:
            bool: erased or not
        """
        if x not in self.d or self.d[x] == 0:
            return False
            # print(x,"is not in HeapDict")
            # raise Exception
            # exit()
        else:
            self.d[x] -= 1
        while len(self.heaplist) != 0:
            if self.d[self.heaplist[0]] == 0:
                heappop(self.heaplist)
            else:
                break
        return True

    def exist(self, x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    @property
    def min(self):
        return self.heaplist[0]

    @property
    def sum(self):
        return sum([k * v for k, v in self.d.items()])


class UnionFindTree:
    """union find tree class
    TODO: fix this description...
    how to use (example):
    >>  uf = UnionFindTree(N) 
    >>  if uf.find_root(a) == uf.find_root(b):
    >>      do something like:
    >>      pass
    >>  else:
    >>      do something like:
    >>      L[uf.find_root(a)] = L[uf.find_root(a)] + L[uf.find_root(b)]
    >>      L[uf.find_root(b)] = L[uf.find_root(a)]
    >>      
    >>      uf.unite(a, b)
    """
    def __init__(self, N):
        self.root = [-1] * (N + 1)
        self.rank = [0] * (N + 1)
        self.connected_num = [1] * (N + 1)

    def find_root(self, x):
        root = self.root
        while root[x] != -1:
            x = root[x]
        return x

    def unite(self, x, y):
        root = self.root
        rank = self.rank
        connected_num = self.connected_num
        find_root = self.find_root

        rx = find_root(x)
        ry = find_root(y)
        if rx != ry:
            if rank[rx] < rank[ry]:
                root[rx] = ry
                rx, ry = ry, rx
            else:
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
                root[ry] = rx
            connected_num[rx] += connected_num[ry]


class UnionFindTree2:
    """union find tree class with specific list
    TODO: fix this description...
    how to use (example):
    >>  uf = UnionFindTree2(N, [1 for _ in range(N)]) 
    >>  if uf.find_root(a) == uf.find_root(b):
    >>      do something like:
    >>      pass
    >>  else:
    >>      do something like:
    >>      uf.unite(a, b, operator.add)
    >>      # L[uf.find_root(a)] = operator.add(L[uf.find_root(a)], L[uf.find_root(b)])
    >>      # L[uf.find_root(b)] = L[uf.find_root(a)]
 
    >>  uf = UnionFindTree2(N, [1 for i in range(N)])
    >>  uf.unite(0, 1, lambda x, y: x+y)
    >>  uf.find_root(0) == uf.find_root(1) # True
    >>  uf.find_root(0) == uf.find_root(2) # False
    >>  uf.find_L(0) # 2 => self.L[self.find_root(i)]
    >>  uf.find_L(1) # 2
    >>  uf.find_L(2) # 1
    
    """
    def __init__(self, N, L):
        self.root = [-1] * (N + 1)
        self.rank = [0] * (N + 1)
        self.connected_num = [1] * (N + 1)
        self.__L = L

    def find_root(self, x):
        root = self.root
        while root[x] != -1:
            x = root[x]
        return x

    def unite(self, x, y, f):
        root = self.root
        rank = self.rank
        connected_num = self.connected_num
        find_root = self.find_root

        # merge L
        L = self.__L
        L[self.find_root(x)] = f(L[self.find_root(x)], L[self.find_root(y)])
        L[self.find_root(y)] = L[self.find_root(x)]

        rx = find_root(x)
        ry = find_root(y)
        if rx != ry:
            if rank[rx] < rank[ry]:
                root[rx] = ry
                rx, ry = ry, rx
            else:
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
                root[ry] = rx
            connected_num[rx] += connected_num[ry]

    def find_L(self, i):
        return self.__L[self.find_root(i)]


class UnionFindTree3:
    """union find tree class with specific list
    ref: https://atcoder.github.io/ac-library/master/document_ja/dsu.html
    ref: https://atcoder.jp/contests/abc177/tasks/abc177_d
    prob: groups -> https://atcoder.jp/contests/arc106/tasks/arc106_b
    # TODO: lambda x, y: 2*x+yみたいなのが果たしてうまく機能するのかはちょっと心配。

    >>> uf = UnionFindTree3(3, [1 for i in range(3)], lambda x, y: 2*x+y) # O(n)
    >>> uf.merge(0, 1)
    >>> uf.leader(0) == uf.leader(1)
    True
    >>> uf.same(0, 1)
    True
    >>> uf.leader(0) == uf.leader(2)
    False
    >>> uf.L(0)
    3
    >>> uf.L(1)
    3
    >>> uf.L(2)
    1
    >>> uf.size(2)
    1
    >>> uf.size(1)
    2
    >>> uf.groups() # O(n)
    [[0, 1], [2]]

    """
    def __init__(self, N, L=None, merge=lambda x, y: x + y):
        self.N = N
        self.root = [-1] * (N + 1)
        self.rank = [0] * (N + 1)
        self.__size = [1] * (N + 1)
        self.__L = L
        self.__merge = merge

    def leader(self, x):
        root = self.root
        while root[x] != -1:
            x = root[x]
        return x

    def merge(self, x, y):
        """xとyが非連結の場合、連結する。Lを初期設定している場合、merge functionに基づいてLも結合する。

        Args:
            x (int): node
            y (int): node
        """
        root = self.root
        rank = self.rank
        __size = self.__size
        leader = self.leader
        L = self.__L

        rx = leader(x)
        ry = leader(y)
        if rx != ry:
            if L is not None:  # merge L
                L[rx] = self.__merge(L[rx], L[ry])
                L[ry] = L[rx]
            if rank[rx] < rank[ry]:
                root[rx] = ry
                rx, ry = ry, rx
            else:
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
                root[ry] = rx
            __size[rx] += __size[ry]
            # if L is not None:
            #     L[rx] = self.__merge(L[rx], L[ry])

    def size(self, i):
        return self.__size[self.leader(i)]

    def L(self, i):
        return self.__L[self.leader(i)]

    def same(self, i, j):
        return self.leader(i) == self.leader(j)

    def groups(self):
        checked = [-1] * self.N
        cnt = 0
        _groups = []
        for i in range(self.N):
            if checked[self.leader(i)] == -1:
                checked[self.leader(i)] = cnt
                cnt += 1
                _groups.append([i])
            else:
                _groups[checked[self.leader(i)]].append(i)
        return _groups


# c++ set
# https://nagiss.hateblo.jp/entry/2020/09/08/203701
class BalancingTree:
    """
    https://qiita.com/Kiri8128/items/6256f8559f0026485d90
    構築はO(1)
    >>  BT = BalancingTree(5) # 0 ～ 30 までの要素を入れられるピボット木
    >>  BT.append(3)
    >>  BT.append(20)
    >>  BT.append(5)
    >>  BT.append(10)
    >>  BT.append(13)
    >>  BT.append(8)
    >>  BT.delete(20)
    >>  print(BT.find_l(12)) # 10
    >>  print(BT.find_r(5)) # 8
    >>  print(BT.min) # 3
    >>  print(BT.max) # 13
    >>  print(3 in BT) # True
    >>  print(4 in BT) # False
    """
    def __init__(self, n):
        self.N = n
        self.root = self.node(1 << n, 1 << n)

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1,
                    nd_.left.value - 1 if nd_.left else -1,
                    nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re

        print("Debug - root =", self.root.value - 1,
              debug_node(self.root)[:50])

    def append(self, v):  # v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p) // 2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p) // 2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v):  # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v):  # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1 << self.N) - 1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd=None, prev=None):  # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return
        if (not nd.left) and (not nd.right):
            if nd.value < prev.value:
                prev.left = None
            else:
                prev.right = None
        elif not nd.left:
            if nd.value < prev.value:
                prev.left = nd.right
            else:
                prev.right = nd.right
        elif not nd.right:
            if nd.value < prev.value:
                prev.left = nd.left
            else:
                prev.right = nd.left
        else:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None


# BalancingTreeを使いやすくしたつもり。3より速いがバグが含まれるらしい。
class BalancingTree2:
    """
    ref: https://qiita.com/Kiri8128/items/6256f8559f0026485d90
    ref: https://atcoder.jp/contests/abc140/tasks/abc140_f
    構築はO(1)
    >>> BT = BalancingTree2(-20, 25) # 少なくとも-20 ~ 25の整数を格納できるBT
    >>> BT.max
    -21
    >>> BT.append(3)
    >>> BT.append(20)
    >>> BT.append(5)
    >>> BT.append(10)
    >>> BT.append(13)
    >>> BT.append(8)
    >>> BT.delete(20)
    >>> BT.append(-5)
    >>> BT.append(-20)
    >>> BT.append(25)
    >>> BT.find_l(12)
    10
    >>> BT.find_r(5)
    8
    >>> BT.min
    -20
    >>> BT.max 
    25
    >>> 3 in BT
    True
    >>> 4 in BT
    False
    """
    def __init__(self, v_least, v_most):
        self.v_least = v_least
        self.v_most = v_most
        self.shift = 1 - self.v_least  # 内部では1~1+(v_most-v_least)を持つ
        self.N = 1 << (v_most - v_least + 1).bit_length()
        self.root = self.node(self.N, self.N)
        self.d = defaultdict(int)

    # def debug(self):
    #     def debug_info(nd_):
    #         return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

    #     def debug_node(nd):
    #         re = []
    #         if nd.left:
    #             re += debug_node(nd.left)
    #         if nd.value: re.append(debug_info(nd))
    #         if nd.right:
    #             re += debug_node(nd.right)
    #         return re
    #     print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def append(self, v):  # v を追加
        assert self.v_least <= v <= self.v_most, f"value must be between {self.v_least} and {self.v_most}"
        iv = v + self.shift  # internal value
        nd = self.root
        if self.d[v] > 0:
            self.d[v] += 1
            return 0
        else:
            self.d[v] = 1
        while True:
            if iv == nd.value:
                # iv がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(iv, nd.value), max(iv, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        iv = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p) // 2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        iv = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p) // 2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v):  # vより真に小さいやつの中での最大値（なければ最小値-1）
        iv = v + self.shift
        nd = self.root
        prev = 0
        if nd.value < iv: prev = nd.value
        while True:
            if iv <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - self.shift
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - self.shift

    def find_r(self, v):  # vより真に大きいやつの中での最小値（なければRoot）
        iv = v + self.shift
        nd = self.root
        prev = 0
        if nd.value > iv: prev = nd.value
        while True:
            if iv < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - self.shift
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - self.shift

    @property
    def max(self):
        return self.find_l(self.N - self.shift)

    @property
    def min(self):
        return self.find_r(-self.shift)

    def delete(self, v, nd=None, prev=None):  # 値がvのノードがあれば削除（なければ何もしない）
        iv = v + self.shift
        if self.d[v] > 1 and nd is None:
            self.d[v] -= 1
            return
        elif not self.d[v] and nd is None:
            return
        else:
            if nd is None:
                del self.d[v]
            if nd is None: nd = self.root
            if prev is None: prev = nd
            while v != nd.value:
                prev = nd
                if v <= nd.value:
                    if nd.left:
                        nd = nd.left
                    else:
                        return
                else:
                    if nd.right:
                        nd = nd.right
                    else:
                        return
            if (nd.left is None) and (nd.right is None):
                if nd.value < prev.value:
                    prev.left = None
                else:
                    prev.right = None
            elif nd.left is None:
                if nd.value < prev.value:
                    prev.left = nd.right
                else:
                    prev.right = nd.right
            elif nd.right is None:
                if nd.value < prev.value:
                    prev.left = nd.left
                else:
                    prev.right = nd.left
            else:
                nd.value = self.leftmost(nd.right).value
                self.delete(nd.value - self.shift, nd.right, nd)

    def __contains__(self, v: int) -> bool:
        # return self.find_r(v - self.shift) == v
        return self.d[v] >= 1

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None


class BalancingTree3:
    """
    ref: https://qiita.com/Kiri8128/items/6256f8559f0026485d90
    ref: https://atcoder.jp/contests/abc140/tasks/abc140_f
    ref: https://atcoder.jp/contests/cpsco2019-s1/tasks/cpsco2019_s1_e
    ref: https://atcoder.jp/contests/abc140/tasks/abc140_e
    
    構築はO(1)
    >>> BT = BalancingTree3(-20, 26) # 少なくとも-20 ~ 26の整数を格納できるBT
    >>> BT.max
    -21
    >>> BT.append(3)
    >>> BT.append(20)
    >>> BT.append(5)
    >>> BT.append(10)
    >>> BT.append(13)
    >>> BT.append(8)
    >>> BT.delete(20)
    >>> BT.append(-5)
    >>> BT.append(-20)
    >>> BT.append(25)
    >>> BT.find_l(12)
    10
    >>> BT.find_r(5)
    8
    >>> BT.find_r(25)
    27
    >>> BT.min
    -20
    >>> BT.max 
    25
    >>> 3 in BT
    True
    >>> 4 in BT
    False
    >>> BT.append(26)
    >>> BT.find_r(25)
    26
    >>> BT.find_r(26)
    27
    >>> BT.append(28)
    Traceback (most recent call last):
        ...
    AssertionError: value must be between -20 and 26
    >>> BT.count(3)
    1
    >>> BT.append(3)
    >>> BT.count(3)
    2
    """
    def __init__(self, v_least, v_most):
        self.v_least = v_least
        self.v_most = v_most
        self.shift = 1 - self.v_least  # 内部では1~1+(v_most-v_least)を持つ
        self.N = 1 << (v_most - v_least + 1).bit_length()
        self.root = self.node(self.N, self.N)
        self.d = defaultdict(int)

    def count(self, v):
        return self.d[v]

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - self.shift, nd_.pivot - self.shift,
                    nd_.left.value - self.shift if nd_.left else -self.shift,
                    nd_.right.value - self.shift if nd_.right else -self.shift)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re

        print("Debug - root =", self.root.value - self.shift,
              debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(nd.value - self.shift)
            if nd.right:
                re += debug_node(nd.right)
            return re

        return debug_node(self.root)[:-1]

    def append(self, v):  # v を追加
        assert self.v_least <= v <= self.v_most, f"value must be between {self.v_least} and {self.v_most}"
        iv = v + self.shift  # internal value
        nd = self.root
        if self.d[v] > 0:
            self.d[v] += 1
            return
        else:
            self.d[v] = 1
        while True:
            if iv == nd.value:
                # iv がすでに存在する場合に何か処理が必要ならここに書く
                return
            else:
                mi, ma = min(iv, nd.value), max(iv, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        iv = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p) // 2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        iv = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p) // 2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v):
        """vより真に小さいやつの中での最大値（なければ最小値-1）

        Args:
            v (int): value

        Returns:
            int: vより真に小さいやつの中での最大値（なければ最小値-1）
        """
        iv = v + self.shift
        nd = self.root
        prev = 0
        if nd.value < iv: prev = nd.value
        while True:
            if iv <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - self.shift
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - self.shift

    def find_r(self, v):
        """vより真に大きいやつの中での最小値（なければself.v_most+1）
        
        # 実装追加したことでRootとv_most+1が異なってしまったので、Rootではなくv_most+1を返してくれたほうが都合が良くなってしまった。
        https://atcoder.jp/contests/abc140/tasks/abc140_e

        Args:
            v (int): value

        Returns:
            int: vより真に大きいやつの中での最小値（なければself.v_most+1）
        """
        if v > self.v_most: return self.v_most + 1  # 追加した
        iv = v + self.shift
        nd = self.root
        prev = 0
        if nd.value > iv: prev = nd.value
        while True:
            if iv < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return min(prev - self.shift, self.v_most + 1)
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return min(prev - self.shift, self.v_most + 1)

    @property
    def max(self):
        return self.find_l(self.N - self.shift)

    @property
    def min(self):
        return self.find_r(-self.shift)

    def delete(self, v, nd=None, prev=None):  # 値がvのノードがあれば削除（なければ何もしない）
        iv = v + self.shift
        if self.d[v] > 1 and nd is None:
            self.d[v] -= 1
            return
        elif not self.d[v] and nd is None:
            return
        else:
            if nd is None:
                del self.d[v]
                nd = self.root
            if prev is None: prev = nd
            while iv != nd.value:
                prev = nd
                if iv <= nd.value:
                    if nd.left:
                        nd = nd.left
                    else:
                        return
                else:
                    if nd.right:
                        nd = nd.right
                    else:
                        return
            if (nd.left is None) and (nd.right is None):
                if prev.left is None:
                    prev.right = None
                elif prev.right is None:
                    prev.left = None
                else:
                    if nd.pivot == prev.left.pivot:
                        prev.left = None
                    else:
                        prev.right = None
            elif nd.right:
                nd.value = self.leftmost(nd.right).value
                self.delete(nd.value - self.shift, nd.right, nd)
            else:
                nd.value = self.rightmost(nd.left).value
                self.delete(nd.value - self.shift, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        # return self.find_r(v - self.shift) == v
        return self.d[v] >= 1

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None


# 2次元累積和
class Accum2D:
    """2次元[N, M]累積和listの作成O(NM)
    2次元累積和の範囲合計の計算O(1)
    
    problem: https://atcoder.jp/contests/abc086/tasks/arc089_b
    accum_2d = Accum2D(images, 2*K, 4*K)
    accum_2d.query(i, i+K, j, j+K)
    """
    def __init__(self, L: List[List[int]], x: int, y: int):
        self.L_acc = self.accumulate_2d(L, x, y)

    @staticmethod
    def accumulate_2d(L: List[List[int]], x: int, y: int) -> List[List[int]]:
        # 高速ゼータ変換: https://qiita.com/convexineq/items/afc84dfb9ee4ec4a67d5
        A = [l for l in L]
        for i in range(x):
            for j in range(y):
                if i: A[i][j] += A[i - 1][j]
        for i in range(x):
            for j in range(y):
                if j: A[i][j] += A[i][j - 1]
        return A

    @staticmethod
    def accumulate_2d_(L: List[List[int]], x: int, y: int) -> List[List[int]]:
        L_acc = [[0] * y for _ in range(x)]
        for i in range(x):
            for j in range(y):
                if i == 0 and j == 0:
                    L_acc[i][j] = L[i][j]
                elif i == 0:
                    L_acc[i][j] = L_acc[i][j - 1] + L[i][j]
                elif j == 0:
                    L_acc[i][j] = L_acc[i - 1][j] + L[i][j]
                else:
                    L_acc[i][j] = L[i][j] + L_acc[i][j - 1] + L_acc[
                        i - 1][j] - L_acc[i - 1][j - 1]
        return L_acc

    def query(self, top: int, bottom: int, left: int, right: int) -> int:
        """sum of 2d list [top, bottom) [left, right))

        Args:
            top (int): [description]
            bottom (int): [description]
            left (int): [description]
            right (int): [description]

        Returns:
            int: [description]
        """
        if top == left == 0:
            return self.L_acc[bottom - 1][right - 1]
        elif top == 0:
            return self.L_acc[bottom - 1][right - 1] - self.L_acc[bottom -
                                                                  1][left - 1]
        elif left == 0:
            return self.L_acc[bottom - 1][right - 1] - self.L_acc[top -
                                                                  1][right - 1]
        else:
            return self.L_acc[bottom - 1][right - 1] - self.L_acc[bottom - 1][
                left - 1] - self.L_acc[top - 1][right -
                                                1] + self.L_acc[top - 1][left -
                                                                         1]


# Binary Indexed Tree (Fenwick Tree; フェニック木)
# 数列A1,..Anが与えられたときに以下のそれぞれをO(logN)で実現するデータ構造
# 要素の更新：任意のi, xに対してAi += x を行う
# 部分和：任意のiに対して A1+A2+..+Aiの値を求める
class BIT:
    # https://juppy.hatenablog.com/entry/2018/11/17/%E8%9F%BB%E6%9C%AC_python_Binary_Indexed_Tree_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0
    # SegTreeより軽いので積極的に使う
    # 外形上は0-indexだが内部は1-indexなのが少しややこしい。
    # BIT_RSQ_RAQがこのクラスを使っているので変更時は注意する。
    def __init__(self, N):
        self.N = N + 1
        self.bit = [0] * (N + 1)

    def __query__(self, i):
        # return sum of [0, i]
        # return 0 if i == -1
        res = 0
        idx = i + 1
        while idx:
            res += self.bit[idx]
            idx -= idx & (-idx)  # 最後に立っている 1 のビットを減算
        return res

    def query(self, l, r=-1):
        """sum of [l, r) if r else [0, l+1)

        Args:
            l (int): left
            r (int, optional): right. Defaults to -1.

        Returns:
            int: sum of [l, r) if r else [0, l+1)
        """
        if r == -1:
            return self.__query__(l)
        else:
            return self.__query__(r - 1) - self.__query__(l - 1)

    def add(self, i, x):
        """Ai += x: O(log N)

        Args:
            i (int): index
            x (int): value
        """
        idx = i + 1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx & (-idx)  # 最後に立っている 1 のビットを加算

    def update(self, i, x):
        """Ai = x: O(log N)
        未検証, use add instead.

        Args:
            i (int): index
            x (int): value
        """
        x = x - self.query(i, i + 1)
        idx = i + 1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx & (-idx)

    def lower_left(self, w):
        """min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0): O(log N)

        Args:
            w (int): value to be found

        Returns:
            int: min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0): O(log N)
        """
        if (w < 0):
            return -1
        x = 0
        k = 1 << (self.N.bit_length() - 1)
        while k > 0:
            if x + k < self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x


class BIT_RSQ_RAQ:
    """区間加算(Range Sum Query), 区間取得(Range Add Query)をO(logN)で答えるBIT組み合わせ
    ref: https://algo-logic.info/binary-indexed-tree/ 区間加算(RAQ)対応 BIT
    Args:
        N (int): number of nodes
    """
    def __init__(self, N):
        """
        Args:
            N (int): number of nodes
        """
        self.N = N
        self.bit0 = BIT(N)
        self.bit1 = BIT(N)

    def __query__(self, i):
        """sum of [0, i]

        Args:
            i (int): right end (included)

        Returns:
            int: sum of [0, i]
        """
        return self.bit0.query(i) + self.bit1.query(i) * i

    def query(self, l, r=-1):
        """sum of [l, r) if r else [0, l+1) (logN)

        Args:
            l ([int]): left side
            r (int, optional): right side. Defaults to -1.

        Returns:
            int: sum of [l, r) if r else [0, l+1)
        """
        if r == -1:
            return self.__query__(l)
        else:
            return self.__query__(r - 1) - self.__query__(l - 1)

    def add(self, val, l, r=-1):
        """add val to [l, r) if r!=-1 else [l, l+1)

        Args:
            val (int or float?): val
            l (int): left
            r (int): right
        """
        if r == -1:
            r = l + 1
        # add val to [l, r): O(logN)
        self.bit0.add(l, -val * (l - 1))
        self.bit0.add(r, val * (r - 1))
        self.bit1.add(l, val)
        self.bit1.add(r, -val)

    def lower_left(self, w):
        """max_i satisfying {Ai < w} (Ai >= 0): O((log N)**2)
        TODO: 実装正しいか不安だが下記は通った。
        ref: https://atcoder.jp/contests/arc033/tasks/arc033_3
        本当はlog Nにできるようだが本実装のほうが分かりやすかった。
        TODO: {A0 ~ Ai < w}も欲しいと思う
        TODO: BITのlower_leftと名前同一機能不一致で分かりにくい。

        Args:
            w (int): value to be found (assume w>=0)

        Returns:
            int: min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0): O(log N)
        """
        if (w < 0):
            return -1
        x = 0
        k = 1 << (self.N.bit_length() - 1)
        while k > 0:
            if x + k < self.N and self.query(x + k, x + k + 1) < w:
                x += k
            k //= 2
        return x


class BIT_Injectable:
    """ref: https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree
    XOR, 掛け算, （欠陥ありで）max, minが載せられる
    初期値と演算する関数を外部注入できるようにした実装。
    identity_factory にはlistやdictなどを載せられるようにするため「引数無しで呼ぶと初期値を生成して返す関数」を書くとのことだがそもそもlistを載せるケースが良くわからない。
    """
    def __init__(self, n, identity_factory, func):
        self.size = n
        self.tree = [identity_factory() for _ in range(n + 1)]
        self.func = func
        self.idf = identity_factory

    def add(self, i, x):
        tree = self.tree
        func = self.func
        while i <= self.size:
            tree[i] = func(tree[i], x)
            i += i & -i

    def sum(self, i):
        s = self.idf()
        tree = self.tree
        func = self.func
        while i > 0:
            s = func(s, tree[i])
            i -= i & -i
        return s


class SegTree_Mine:
    """
    TODO: 機能拡充：https://ei1333.hateblo.jp/entry/2017/12/14/000000
    TODO: 機能拡充：https://atcoder.github.io/ac-library/document_ja/segtree.html
    ref: https://qiita.com/takayg1/items/c811bd07c21923d7ec69
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    
    操作	    segfunc	        単位元
    最小値	    min(x, y)	    float('inf')
    最大値	    max(x, y)	    -float('inf')
    区間和	    x + y	        0
    区間積	    x * y	        1
    最大公約数	math.gcd(x, y)	0
    
    >>> seg = SegTree_Mine([14, 5, 9, 13], min, float('inf'))
    >>> seg.query(0, 4) # get segfunc([l, r))
    5
    >>> seg.mindex(0, 4) # get decisive index and its value in ([0, 4))
    (1, 5)
    >>> seg.add(1, 3) # add value of pos 2 to 3
    >>> seg.query(0, 4)
    8
    >>> seg.update(1, 3) # update value of pos 2 to 3
    >>> seg.query(0, 4)
    3

    >>> seg = SegTree_Mine([14, 5, 9, 13], lambda x, y: x+y, 0)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def mindex(self, l, r):
        """find ([far left] index, value) where the query value in [l, r) is decided by the index when self.segfunc = min, max etc.
        ex: [8, 6, 3, 5, 9, 3], segfunc = min: => return (2, 3) (left minimum value "3" is placed at 2)
        O(log N) 
        ref: https://atcoder.jp/contests/abc194/tasks/abc194_e
        ref: https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c
        ref: https://atcoder.jp/contests/abc116/tasks/abc116_c

        Args:
            l (int): index(0-index)
            r (int): index(0-index)
        """

        # ver O((log N)**2)
        # v = self.query(l, r)
        # bin = [l, r] # [l, r)
        # while bin[1]-bin[0] > 1:
        #     mid = (bin[1]+bin[0])//2
        #     if v == self.query(bin[0], mid):
        #         bin[1] = mid
        #     else:
        #         bin[0] = mid
        # return (v, bin[0])

        # queryと同じ要領でtreeを登りつつ、値が更新されるか、値が同じでかつ範囲がより左の部分であるような範囲が見つかった場合にそのvalue, indexを記録する。
        # 値が同じだった場合に範囲が左かどうかは、前回更新時に左で更新されていたら前回のほうが範囲が左、前回更新時に右で更新されていたら今回のほうが範囲が左となる。範囲の両端から見られていくため。

        res = self.ide_ele
        l += self.num
        r += self.num

        # candidate # 初期値はcand_pos=INFのように、弱く設定する方が自然に感じるが、cand_v以外は強くて小さい値にすると処理が速くなるっぽい。
        cand_v = res
        cand_pos = l
        cand_right = True
        cand_hight = 0
        current_hight = 0

        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                if (res != cand_v) or (res == self.segfunc(
                        self.ide_ele, self.tree[l]) and cand_right == False):
                    cand_v = res
                    cand_right = True
                    cand_pos = l
                    cand_hight = current_hight
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
                if (res != cand_v) or (res == self.segfunc(
                        self.ide_ele, self.tree[r - 1])
                                       and cand_right == False):
                    cand_v = res
                    cand_right = False
                    cand_pos = r - 1
                    cand_hight = current_hight
            l >>= 1
            r >>= 1
            current_hight += 1

        # cand_hight>0の場合、cand_posは1点ではなく範囲を意味するため、treeを降りつつ点[l, l+1)を特定する。
        while cand_hight:
            cand_hight -= 1
            if self.tree[cand_pos * 2] == cand_v:
                cand_pos = cand_pos * 2
            else:
                cand_pos = cand_pos * 2 + 1

        return (cand_pos - self.num, cand_v)

    def update(self, k, v):
        """
        k番目の値をxに更新
        k: index(0-index)
        v: update value
        """
        k += self.num
        self.tree[k] = v
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def add(self, k, v):
        """
        k番目の値にxをadd
        k: index(0-index)
        v: update value
        """
        k += self.num
        self.tree[k] += v
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


class SegTree:
    """[summary]

    N, Q = R()
    A = R()
    seg = SegTree(max, -float('inf'), A)

    for _ in range(Q):
        t, x, v = R()
        if t == 1:
            seg.set(x-1, v)
        elif t == 2:
            l, r = x-1, v
            print(seg.prod(l, r))
        else:
            print(seg.max_right(x-1, lambda x: x<v)+1)
    """
    def __init__(self, op: typing.Callable[[typing.Any, typing.Any],
                                           typing.Any], e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _ceil_pow2(self, n: int) -> int:
        x = 0
        while (1 << x) < n:
            x += 1

        return x

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int, f: typing.Callable[[typing.Any],
                                                      bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: typing.Callable[[typing.Any],
                                                      bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


class SegTree2D:
    """ref: https://qiita.com/tomato1997/items/83ccdfe0ce1f5548a42a
    ref: https://atcoder.jp/contests/abc086/tasks/arc089_b
    ref: 10**6程度でTLEしてしまったからなかなか使い所が難しい
    N, M, 2D List, func (pick up char from min,max,sum,prd(product),gcd,lmc,^,&,|)

    """
    DEFAULT = {
        'min': 1 << 60,
        'max': -(1 << 60),
        'sum': 0,
        'prd': 1,
        'gcd': 0,
        'lmc': 1,
        '^': 0,
        '&': (1 << 60) - 1,
        '|': 0,
    }

    FUNC = {
        'min': min,
        'max': max,
        'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y),
        'gcd': gcd,
        'lmc': (lambda x, y: (x * y) // gcd(x, y)),
        '^': (lambda x, y: x ^ y),
        '&': (lambda x, y: x & y),
        '|': (lambda x, y: x | y),
    }

    def __init__(self, N, M, ls2D, mode='min'):
        self.default = self.DEFAULT[mode]
        self.func = self.FUNC[mode]
        self.N = N
        self.M = M
        self.KN = (N - 1).bit_length()
        self.KM = (M - 1).bit_length()
        self.N2 = 1 << self.KN
        self.M2 = 1 << self.KM
        self.data = [[self.default] * (2**(self.KM + 1))
                     for i in range(2**(self.KN + 1))]
        for i in range(self.N):
            for j in range(self.M):
                self.data[self.N2 + i][self.M2 + j] = ls2D[i][j]
        self.__build()

    def __build(self):
        for j in range(self.M):
            for i in range(self.N2 - 1, 0, -1):
                self.data[i][self.M2 + j] = self.func(
                    self.data[i << 1][self.M2 + j],
                    self.data[i << 1 | 1][self.M2 + j])
        for i in range(2**(self.KN + 1)):
            for j in range(self.M2 - 1, 0, -1):
                self.data[i][j] = self.func(self.data[i][j << 1],
                                            self.data[i][j << 1 | 1])

    def leafvalue(self, x, y):  # (x,y)番目の値の取得
        return self.data[x + self.N2][y + self.M2]

    def update(self, x, y, value):  # (x,y)の値をvalueに変える
        """change value of (x, y) to value

        Args:
            x (int): x of (x, y)
            y (int): y of (x, y)
            value (int): value
        """
        i = x + self.N2
        j = y + self.M2
        self.data[i][j] = value
        while j > 1:
            j >>= 1
            self.data[i][j] = self.func(self.data[i][j << 1],
                                        self.data[i][j << 1 | 1])
        j = y + self.M2
        while i > 1:
            i >>= 1
            self.data[i][j] = self.func(self.data[i << 1][j],
                                        self.data[i << 1 | 1][j])
            while j > 1:
                j >>= 1
                self.data[i][j] = self.func(self.data[i][j << 1],
                                            self.data[i][j << 1 | 1])
            j = y + self.M2
        return

    def query(self, Lx, Rx, Ly, Ry):
        """value of [Lx,Rx)×[Ly,Ry)

        Args:
            Lx (int): left of x
            Rx (int): right of x
            Ly (int): left of y
            Ry (int): right of y

        Returns:
            int: value
        """
        Lx += self.N2
        Rx += self.N2
        Ly += self.M2
        Ry += self.M2
        vLx = self.default
        vRx = self.default
        while Lx < Rx:
            if Lx & 1:
                vLy = self.default
                vRy = self.default
                Ly1 = Ly
                Ry1 = Ry
                while Ly1 < Ry1:
                    if Ly1 & 1:
                        vLy = self.func(vLy, self.data[Lx][Ly1])
                        Ly1 += 1
                    if Ry1 & 1:
                        Ry1 -= 1
                        vRy = self.func(self.data[Lx][Ry1], vRy)
                    Ly1 >>= 1
                    Ry1 >>= 1
                vy = self.func(vLy, vRy)
                vLx = self.func(vLx, vy)
                Lx += 1
            if Rx & 1:
                Rx -= 1
                vLy = self.default
                vRy = self.default
                Ly1 = Ly
                Ry1 = Ry
                while Ly1 < Ry1:
                    if Ly1 & 1:
                        vLy = self.func(vLy, self.data[Rx][Ly1])
                        Ly1 += 1
                    if Ry1 & 1:
                        Ry1 -= 1
                        vRy = self.func(self.data[Rx][Ry1], vRy)
                    Ly1 >>= 1
                    Ry1 >>= 1
                vy = self.func(vLy, vRy)
                vRx = self.func(vy, vRx)
            Lx >>= 1
            Rx >>= 1
        return self.func(vLx, vRx)


# CHT, LiChaoTree
class LiChaoTree:
    """
    ref: https://atcoder.jp/contests/dp/submissions/17399987
    ref: https://atcoder.jp/contests/dp/tasks/dp_z
    ref: # 線分追加の実装
        https://smijake3.hatenablog.com/entry/2018/06/16/144548        
        https://maspypy.com/segment-tree-%e3%81%ae%e3%81%8a%e5%8b%89%e5%bc%b71#toc6
        問題：https://atcoder.jp/contests/abc076/tasks/abc076_d

    >>> lct = LiChaoTree([1, 2, 3, 5, 6, 8]) # X: List of x-axis values to be used for evaluation
    >>> lct.add_line(1, 3) # add 1*x + 3
    >>> lct.add_line(2, -3) # add 2*x - 3
    >>> lct.query(1) # minimum value of lines at x = x1
    -1
    >>> lct.query(2)
    1
    >>> lct.query(3)
    3
    >>> lct.query(5)
    7
    >>> lct.query(6)
    9
    >>> lct.query(8)
    11
    >>> lct.add_line_seg(0, -2, 2, 3) # add 0*x - 2 to interval of x :[2, 3]
    >>> lct.query(2)
    -2
    >>> lct.query(3)
    -2
    >>> lct.query(5)
    7
    """
    def __init__(self, X):
        X = sorted(list(set(X)))
        self.inf = INF
        self.n = 1 << (len(X) - 1).bit_length()
        self.X = X + [self.inf] * (self.n - len(X))
        self.D = {a: i for i, a in enumerate(X)}
        self.lmr = [(0, 0, 0)] * self.n + [(x, x, x) for x in self.X]
        for i in range(1, self.n)[::-1]:
            self.lmr[i] = (self.lmr[i * 2][0], self.lmr[i * 2][2],
                           self.lmr[i * 2 ^ 1][2])
        self.F = [None] * (self.n * 2)

    def _calc(self, f, x):
        return f[0] * x + f[1]

    def _update(self, i, f):
        while 1:
            l, m, r = self.lmr[i]
            fi = self.F[i]
            if fi is None:
                self.F[i] = f
                return
            cl = self._calc(fi, l) > self._calc(f, l)
            cr = self._calc(fi, r) > self._calc(f, r)
            if cl and cr:
                self.F[i] = f
                return
            if not cl and not cr:
                return
            if self._calc(fi, m) > self._calc(f, m):
                self.F[i], f = f, fi
                cl = not cl
            if cl:
                i *= 2
            else:
                i = i * 2 + 1

    def query(self, x):
        """min(a*x + b) at x = x : O(logN)

        Args:
            x (int): value of x-axis

        Returns:
            int: minimum value
        """
        i = self.D[x] + self.n
        mi = self.inf
        while i > 0:
            if self.F[i]:
                mi = min(mi, self._calc(self.F[i], x))
            i >>= 1
        return mi

    def add_line(self, a, b):
        """add line a*x + b : O(logN)

        Args:
            a (int): a of a*x + a
            b (int): b of a*x + b
        """
        f = (a, b)
        self._update(1, f)

    def add_line_seg(self, a, b, x_L, x_R):
        """add line segment a*x + b to interval [x_L, x_R] (closed, not half-open) : O((logN)**2)

        Args:
            a (int): a of a*x + a
            b (int): b of a*x + b
            x_L (int): left edge of line segment
            x_R (int): right edge of line segment
        """
        L = self.D[x_L] + self.n
        R = (self.D[x_R] + 1) + self.n  # half-open section
        f = (a, b)
        while L < R:
            if L & 1:
                self._update(L, f)
                L += 1
            if R & 1:
                R -= 1
                self._update(R, f)
            L >>= 1
            R >>= 1


class LazySegmentTree_RMQ_RAQ():
    """ RMQ and RAQ
    ref: https://atcoder.jp/contests/dp/submissions/16029749 <= この実装。速いしコードがシンプルで綺麗。
    ref: https://atcoder.jp/contests/dp/submissions/12866634 <= 機能が多くて便利そうだが使い方がまだ良くわからない。拡張機能の参考になりそうだがまず理解する必要あり。

    ex: 
    LST=LazySegmentTree(N,[0]*N,merge_func=min,ide_ele=10**18)
    LST.add(i, r+1, v)
    LST.query(0, N)

    そもそも遅延セグ木については…
    ref: https://maspypy.com/segment-tree-%E3%81%AE%E3%81%8A%E5%8B%89%E5%BC%B72 <= 初めに数学分からない人を門前払いしている感じだが諦めずに後ろを読むと非常に具体的でわかりやすい。
    ref: https://tsutaj.hatenablog.com/entry/2017/03/30/224339 <= とてもわかりやすい。具体例のNが小さいためにO(N)みたいに見えるが、Nを大きくして考えてみるとO(logN）っぽさが納得できる。
    
    """
    def __init__(self, n, init, merge_func=min, ide_ele=10**18):
        self.n = (n - 1).bit_length()
        self.merge_func = merge_func
        self.ide_ele = ide_ele
        self.data = [0 for i in range(1 << (self.n + 1))]
        self.lazy = [0 for i in range(1 << (self.n + 1))]
        for i in range(n):
            self.data[2**self.n + i] = init[i]
        for i in range(2**self.n - 1, 0, -1):
            self.data[i] = self.merge_func(self.data[2 * i],
                                           self.data[2 * i + 1])

    def propagate_above(self, i):
        m = i.bit_length() - 1
        for bit in range(m, 0, -1):
            v = i >> bit
            add = self.lazy[v]
            self.lazy[v] = 0
            self.data[2 * v] += add
            self.data[2 * v + 1] += add
            self.lazy[2 * v] += add
            self.lazy[2 * v + 1] += add

    def remerge_above(self, i):
        while i:
            i >>= 1
            self.data[i] = self.merge_func(self.data[2 * i],
                                           self.data[2 * i + 1]) + self.lazy[i]

    def add(self, l, r, x):
        l += 1 << self.n
        r += 1 << self.n
        l0 = l // (l & -l)
        r0 = r // (r & -r) - 1
        while l < r:
            self.data[l] += x * (l & 1)
            self.lazy[l] += x * (l & 1)
            l += (l & 1)
            self.data[r - 1] += x * (r & 1)
            self.lazy[r - 1] += x * (r & 1)
            l >>= 1
            r >>= 1
        self.remerge_above(l0)
        self.remerge_above(r0)

    def query(self, l, r):
        l += 1 << self.n
        r += 1 << self.n
        l0 = l // (l & -l)
        r0 = r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        res = self.ide_ele
        while l < r:
            if l & 1:
                res = self.merge_func(res, self.data[l])
                l += 1
            if r & 1:
                res = self.merge_func(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res


def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class LazySegTree:
    def __init__(self, op: typing.Callable[[typing.Any, typing.Any],
                                           typing.Any], e: typing.Any,
                 mapping: typing.Callable[[typing.Any, typing.Any],
                                          typing.Any],
                 composition: typing.Callable[[typing.Any, typing.Any],
                                              typing.Any], id_: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def apply(self,
              left: int,
              right: typing.Optional[int] = None,
              f: typing.Optional[typing.Any] = None) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left: int, g: typing.Callable[[typing.Any],
                                                      bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id


def slide_max_index(a, K):
    """max_idx[i]: 区間 [i - K + 1, i] (両側閉区間)における a の最大値を与えるインデックス, 長さKに満たない左側領域もついでに計算
    ref: https://qiita.com/kuuso1/items/318d42cd089a49eeb332

    Args:
        a ([list]): 配列
        K ([int]): スライドの長さ

    Returns:
        list, list: max_idx, max_val
    """
    #
    N = len(a)
    max_idx = [0] * N  # (長さKに満たない左側領域もついでに計算する)
    max_val = [0] * N  # (長さKに満たない左側領域もついでに計算する)
    deq = deque()  # デック．番長順番待ちキューをシミュレートする．インデックスを格納しておく

    for i in range(0, N):
        while len(deq) > 0 and deq[0] <= i - K:
            deq.popleft()  # 卒業する
        while len(deq) > 0 and a[deq[-1]] < a[i]:
            deq.pop()  # a[i] の入学で 望みがなくなった先輩達が脱落する
        deq.append(i)  # 新入生i は常に番長になる望みがある
        max_idx[i] = deq[0]  # 番長順番待ちキューの最左が番長
        max_val[i] = a[deq[0]]  # 番長順番待ちキューの最左が番長

    return max_idx, max_val


# ************ Graph ************
# Graph: https://en.wikipedia.org/wiki/Directed_graph
# 最短経路問題: https://ja.wikipedia.org/wiki/%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E5%95%8F%E9%A1%8C
# Visual site (graph×graph): https://hello-world-494ec.firebaseapp.com/ 最初に「nodeの数 辺の数」 次以降 「node node」を入力する。
# ダイクストラ Dijkstra: 各辺が非負のコストを持つときある1つのノードからあるもう一つのノードへの最短経路を求めるやつ。
# Bellman-Ford: O(|V||E|). Use this if there exists an edge with negative length in the graph
# After N steps, the shortest path has converded if there doesn't exist an cycle of edges with negative
# Watch out: d[N] == d[2*N] doesn't necessarily mean the graph doesn't have negative cycle
# ref: https://www.youtube.com/watch?v=1Z6ofKN03_Y


def BellmanFord(N,
                M,
                ABC,
                vertex_start,
                vertex_end,
                value_if_inf=-1,
                find_shortest=False):
    """to calculate furthest or shortest length between vertex_start and vertex_end using BellmanFord algorithm
    
    Args:
        N (int): number of vertices
        M (int): number of edges
        ABC (list): [(ai, bi, ci) for _ in range(N)] where i-th edge is directed from vertex ai to vertex bi and the length is ci 
        vertex_start (int): start vertex. usually use 0.
        vertex_end (int): end vertex. usually use N-1.
        value_if_inf (int or string as you like, optional): value you want when the furthest (or shortest) distance is infinite (or -infinite). Defaults to -1.
        find_shortest (bool, optional): choose False to find furthest path. Defaults to False.
    
    Returns:
        int or string: normally int (but can be str if you set value_if_inf to str)
        
    Example:
            N, M, P = R()
            ABC = [R() for _ in range(M)]
            ABC = [(a-1, b-1, c-P) for a, b, c in ABC]
            print(BellmanFord(N, M, ABC, 0, N-1, value_if_inf = 'inf'))
 
    """
    def make_reachable_list(N, M, ABC, vertex_start, vertex_end):
        reachable_to_direct = defaultdict(list)
        reachable_from_direct = defaultdict(list)
        reachable_from_start = [False] * N
        reachable_to_end = [False] * N
        reachable_from_start[vertex_start] = True
        reachable_to_end[vertex_end] = True
        reachable_from_both_sides = [False] * N
        dfs_from_start = []
        dfs_to_end = []
        for a, b, c in ABC:
            reachable_to_direct[a].append(b)
            reachable_from_direct[b].append(a)
            if a == vertex_start:
                dfs_from_start.append(b)
                reachable_from_start[b] = True
            if b == vertex_end:
                dfs_to_end.append(a)
                reachable_to_end[a] = True
        while dfs_from_start:
            v = dfs_from_start.pop()
            for i in reachable_to_direct[v]:
                if not reachable_from_start[i]:
                    reachable_from_start[i] = True
                    dfs_from_start.append(i)
        while dfs_to_end:
            v = dfs_to_end.pop()
            for i in reachable_from_direct[v]:
                if not reachable_to_end[i]:
                    reachable_to_end[i] = True
                    dfs_to_end.append(i)
        for i in range(N):
            reachable_from_both_sides[
                i] = reachable_from_start[i] and reachable_to_end[i]
        return reachable_from_both_sides

    reachable_from_both_sides = make_reachable_list(N, M, ABC, vertex_start,
                                                    vertex_end)

    if find_shortest:
        dist = [INF for i in range(N)]
    else:
        dist = [-INF for i in range(N)]

    dist[vertex_start] = 0
    for i in range(N):
        updated = False
        for a, b, c in ABC:
            if not reachable_from_both_sides[a]:
                continue
            elif find_shortest:
                update_condition = dist[a] + c < dist[b]
            else:
                update_condition = dist[a] + c > dist[b]
            if dist[a] != INF and update_condition:
                dist[b] = dist[a] + c
                updated = True
                if i == N - 1:
                    return value_if_inf
        if not updated:
            break
    return dist[vertex_end]


# Warshall Floyd O(V**3) # V:vertex(頂点, nodeともいう)
def warshall_floyd(number_vertex,
                   XYD,
                   directed=False,
                   shift_one_for_vertex=False,
                   init_dist=INF):
    """O(V**3)
    # ref: https://juppy.hatenablog.com/entry/2018/11/01/%E8%9F%BB%E6%9C%AC_python_%E5%85%A8%E7%82%B9%E5%AF%BE%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E6%B3%95%EF%BC%88%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95

    Args:
        number_vertex (int): number of vertex(nodes)
        XYD (list): list of distance from x and y
        directed(bool, optional): True if XYD implies direction (only x -> y is approved, and y-> x is banned)
        shift_one_for_vertex (bool, optional): True if XY is 1-indexed. Defaults to False.

    Returns:
        list: d[i][j] is distance from i to j
    """
    d = [[init_dist] * number_vertex for i in range(number_vertex)]
    for x, y, dist in XYD:
        if shift_one_for_vertex:
            x = x - 1
            y = y - 1
        d[x][y] = dist
        if not directed:
            d[y][x] = dist
    for i in range(number_vertex):
        d[i][i] = 0  # distance of same vertex is 0
    for k in range(number_vertex):
        for i in range(number_vertex):
            for j in range(number_vertex):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


# 最短ハミルトン路問題とは，グラフが与えられたとき，全ての頂点を一度ずつ通るパスで，経路長が最短のものを求める問題である．求めるものがパスでなく，サイクルである場合は最短ハミルトン閉路，もしくは巡回セールスマン問題という． O(N^2 2**N) => N=17程度
# ref: http://www.prefield.com/algorithm/graph/shortest_hamilton_path.html
# ref: https://atcoder.jp/contests/abc190/submissions/19832174


# 最小共通祖先
# https://ikatakos.com/pot/programming_algorithm/graph_theory/lowest_common_ancestor
class LcaDoubling:
    """
    links[v] = { (u, w), (u, w), ... }  (u:隣接頂点, w:辺の重み)
    というグラフ情報から、ダブリングによるLCAを構築。
    任意の2頂点のLCAおよび距離を取得できるようにする
    """
    def __init__(self, n, links, root=0):
        self.depths = [-1] * n
        self.distances = [-1] * n
        prev_ancestors = self._init_dfs(n, links, root)
        self.ancestors = [prev_ancestors]
        max_depth = max(self.depths)
        d = 1
        while d < max_depth:
            next_ancestors = [prev_ancestors[p] for p in prev_ancestors]
            self.ancestors.append(next_ancestors)
            d <<= 1
            prev_ancestors = next_ancestors

    def _init_dfs(self, n, links, root):
        q = [(root, -1, 0, 0)]
        direct_ancestors = [-1] * (n + 1
                                   )  # 頂点数より1個長くし、存在しないことを-1で表す。末尾(-1)要素は常に-1
        while q:
            v, p, dep, dist = q.pop()
            direct_ancestors[v] = p
            self.depths[v] = dep
            self.distances[v] = dist
            q.extend((u, v, dep + 1, dist + w) for u, w in links[v] if u != p)
        return direct_ancestors

    def get_lca(self, u, v):
        du, dv = self.depths[u], self.depths[v]
        if du > dv:
            u, v = v, u
            du, dv = dv, du
        tu = u
        tv = self.upstream(v, dv - du)
        if u == tv:
            return u
        for k in range(du.bit_length() - 1, -1, -1):
            mu = self.ancestors[k][tu]
            mv = self.ancestors[k][tv]
            if mu != mv:
                tu = mu
                tv = mv
        lca = self.ancestors[0][tu]
        assert lca == self.ancestors[0][tv]
        return lca

    def get_distance(self, u, v):
        lca = self.get_lca(u, v)
        return self.distances[u] + self.distances[v] - 2 * self.distances[lca]

    def upstream(self, v, k):
        i = 0
        while k:
            if k & 1:
                v = self.ancestors[i][v]
            k >>= 1
            i += 1
        return v


# 部分木に値追加を行うクエリなどに対応できる
class EulerTour:
    """
    N: number of node
    X: connection of each node, 0-index
    i0: root. 多分。
    
    Returns:
        [type]: [description]

    ref: https://qiita.com/Kiri8128/items/2b0023bed9af642c751c
    ref: https://maspypy.com/euler-tour-%E3%81%AE%E3%81%8A%E5%8B%89%E5%BC%B7
    
    ところでEulerTourのナンバーの振り方はバリエーションがあるようだ。その一つで、ノードにInとOutの際にカウントを増やす場合のイメージ図：https://atcoder.jp/contests/abc202/editorial/1864
    """
    def __init__(self, N, X, i0=0):
        self.N = N
        self.i0 = i0
        self.ET, self.In, self.Out, self.Depth = self.EulerTour(X.copy())

    def EulerTour(self, X):
        # Xは破壊してXとPができる
        P = [-1] * self.N
        Q = [~self.i0, self.i0]
        ct = -1
        ET = []
        ET1 = [0] * self.N
        ET2 = [0] * self.N
        DE = [0] * self.N
        de = -1
        while Q:
            i = Q.pop()
            if i < 0:
                # ↓ 戻りも数字を足す場合はこれを使う
                ct += 1
                # ↓ 戻りもETに入れる場合はこれを使う
                ET.append(P[~i])
                ET2[~i] = ct
                de -= 1
                continue
            if i >= 0:
                ET.append(i)
                ct += 1
                if ET1[i] == 0: ET1[i] = ct
                de += 1
                DE[i] = de
            for a in X[i][::-1]:
                if a != P[i]:
                    P[a] = i
                    for k in range(len(X[a])):
                        if X[a][k] == i:
                            del X[a][k]
                            break
                    Q.append(~a)
                    Q.append(a)
        return (ET, ET1, ET2, DE)


# chain decomposition による木の橋(bridge)と関節点(joint point)の探索。(ただ、橋と関節点はlowlinkによる実装が普通みたいです。)
def bridges_and_joint_points(
        G: List[List[int]], N: int) -> Tuple[List[Tuple[int, int]], List[int]]:
    """chain decompositionで木の橋と関節点を求める
    計算量: O(|V|+|E|)
    ref: https://smijake3.hatenablog.com/entry/2019/08/24/164727
    TODO: ロジックの理解
    problem: https://atcoder.jp/contests/abc075/tasks/abc075_c (制約が甘いので全探索でもOKな問題)

    Args:
        G (List[List[int]]): Graph. 良くedges = [list() for _ in range(N)], for a, b in AB: edges[a].append(b) edges[b].append(a)として作っているもの。
        N (int): number of nodes

    Returns:
        Tuple[List[Tuple[int, int]], List[int]]: tuple of Bridges and Joint points
        
    ex:
        # B: グラフGの橋
        # A: グラフGの関節点
        B, A = bridges_and_joint_points(G, N)
    """
    # P[v]: DFS-treeにおける頂点vの親頂点
    P = [0] * N
    # G0: グラフGのbackedgeのみに絞った有向グラフ
    G0 = [[] for i in range(N)]
    # V: 頂点をpre-orderに並べたもの
    V = []

    # P, V, G0 を計算するDFS
    lb = [0] * N

    def dfs(v, p):
        P[v] = p
        V.append(v)
        lb[v] = len(V)
        for w in G[v]:
            if w == p:
                continue
            if lb[w]:
                if lb[v] < lb[w]:
                    # (v, w) は backedge
                    G0[v].append(w)
                continue
            # (v, w) は tree edge
            dfs(w, v)

    dfs(0, -1)

    # B: 橋となる辺e = (u, v) のリスト
    B = []
    # ap[v]: 頂点vが関節点であるか?
    ap = [0] * N

    used = [0] * N
    first = 1
    used[0] = 1
    # グラフの頂点をpre-orderで見ていく
    for u in V:
        if not used[u]:
            # 頂点uは以前に探索されてない
            # -> この親頂点pへのtree edgeがchainとして含まれない
            # -> 辺(u, p) は橋
            p = P[u]
            B.append((u, p) if u < p else (p, u))
            # 橋に隣接し、次数が2以上の頂点は関節点
            if len(G[u]) > 1:
                ap[u] = 1
            if len(G[p]) > 1:
                ap[p] = 1

        # 頂点vが始点となるbackedgeについて調べる
        cycle = 0
        for v in G0[u]:
            # tree edgeに従って根頂点に向かって上がっていく
            w = v
            while w != u and not used[w]:
                used[w] = 1
                w = P[w]
            # このchainはcycle
            if w == u:
                cycle = 1

        if cycle:
            if not first:
                # 2つ目以降のcycle chainである場合、頂点uは関節点
                ap[u] = 1
            first = 0

    A = [v for v in range(N) if ap[v]]
    return B, A


# 強連結成分分解
def scc(N, edges):
    M = len(edges)
    start = [0] * (N + 1)
    elist = [0] * M
    for e in edges:
        start[e[0] + 1] += 1
    for i in range(1, N + 1):
        start[i] += start[i - 1]
    counter = start[:]
    for e in edges:
        elist[counter[e[0]]] = e[1]
        counter[e[0]] += 1
    NG = [0, 0]
    visited = []
    low = [0] * N
    Ord = [-1] * N
    ids = [0] * N

    def dfs(v):
        low[v] = NG[0]
        Ord[v] = NG[0]
        NG[0] += 1
        visited.append(v)
        for i in range(start[v], start[v + 1]):
            to = elist[i]
            if Ord[to] == -1:
                dfs(to)
                low[v] = min(low[v], low[to])
            else:
                low[v] = min(low[v], Ord[to])
        if low[v] == Ord[v]:
            while (True):
                u = visited.pop()
                Ord[u] = N
                ids[u] = NG[1]
                if u == v:
                    break
            NG[1] += 1

    for i in range(N):
        if Ord[i] == -1:
            dfs(i)
    for i in range(N):
        ids[i] = NG[1] - 1 - ids[i]
    group_num = NG[1]
    counts = [0] * group_num
    for x in ids:
        counts[x] += 1
    groups = [[] for i in range(group_num)]
    for i in range(N):
        groups[ids[i]].append(i)
    return groups


class SCCGraph:
    """
    ref: https://github.com/not522/ac-library-python/blob/master/atcoder/scc.py
    
    ex:
    N, M = R()
    AB = Rs(M)
    scc = SCCGraph(N, AB)
    ans = scc.scc()
    print(len(ans))
    for a in ans:
        print(len(a), *a)

    """
    def __init__(
            self,
            n: int = 0,
            edges: typing.Optional[typing.List[typing.List[int]]] = None
    ) -> None:
        self._internal = _SCCGraph(n)
        if edges:
            for from_vertex, to_vertex in edges:
                self.add_edge(from_vertex, to_vertex)

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        n = self._internal.num_vertices()
        assert 0 <= from_vertex < n
        assert 0 <= to_vertex < n
        self._internal.add_edge(from_vertex, to_vertex)

    def scc(self) -> typing.List[typing.List[int]]:
        return self._internal.scc()


class _CSR:
    def __init__(self, n: int, edges: typing.List[typing.Tuple[int,
                                                               int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)

        for e in edges:
            self.start[e[0] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = deepcopy(self.start)
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1


class _SCCGraph:
    '''
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    '''
    def __init__(self, n: int) -> None:
        self._n = n
        self._edges: typing.List[typing.Tuple[int, int]] = []

    def num_vertices(self) -> int:
        return self._n

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self._edges.append((from_vertex, to_vertex))

    def scc_ids(self) -> typing.Tuple[int, typing.List[int]]:
        g = _CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def scc(self) -> typing.List[typing.List[int]]:
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: typing.List[typing.List[int]] = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups


# ************ Tree ************
def topological_sorted_tree(XY, N, root=0):
    """topological sort of tree
    # ref: https://qiita.com/Kiri8128/items/cbaa021dbcb07b5fdb92

    Args:
        XY (list of lists): connection between nodes (0-indexed)
        N (int): number of nodes
        root (int, optional): root of tree. Defaults to 0.

    Returns:
        list, list, list, list: children (=edges without parent node), topologically sorted node, parent index, partial_size
        
    ex: https://atcoder.jp/contests/dp/tasks/dp_p
        N = r_int()
        XY = [R1() for _ in range(N-1)]
        children, topo_sort, parent, partial_size = topological_sorted_tree(XY, N)
        MOD = 10**9+7
        
        dpw = [1]*N
        dpb = [1]*N
        for i in topo_sort[::-1]:
            for child in children[i]:
                dpw[i]*=dpw[child]+dpb[child]
                dpw[i]%=MOD
                dpb[i]*=dpw[child]
                dpb[i]%=MOD
        print((dpw[0]+dpb[0])%MOD)
    """

    children = [list() for _ in range(N)]
    for x, y in XY:
        children[x].append(y)
        children[y].append(x)

    parent = [-1] * N  # parent[i] はiの親。iが根なら-1
    Q = deque([root])  # queue。根にするやつを最初に追加
    topo_sort = []  # トポロジカルソート
    while Q:
        i = deque.popleft(Q)
        topo_sort.append(i)
        for a in children[i]:
            if a == parent[i]: continue
            parent[a] = i
            children[a].remove(i)
            deque.append(Q, a)

    partial_size = [1] * N
    for i in topo_sort[:0:-1]:
        partial_size[parent[i]] += partial_size[i]
    return children, topo_sort, parent, partial_size


# 全方位木DP(rerooting)
def retooting(X, Topo, P, N, unit, merge, adj_bu, adj_td, adj_fin, root=0):
    """全方位DP
    # ref: https://qiita.com/Kiri8128/items/a011c90d25911bdb3ed3
    # ref: https://atcoder.jp/contests/dp/submissions/19898045

    Args:
        X (list): [description]
        Topo (list): [description]
        P (list): [description]
        N (int): [description]
        unit ([type]): [description]
        merge ([type]): function used to merge to dp.
        adj_bu ([type]): function used after merged.DPの遷移がf(i)=Σmerge(j:= iの子)+g(i)と表せるときのg(i)部分、みたいなイメージ
        adj_td ([type]): function used after merged.DPの遷移がf(i)=merge(j:= iの親)+g(i)と表せるときのg(i)部分
        adj_fin ([type]): function finally used
        root (int, optional): [description]. Defaults to 0.

    Returns:
        list: result of rerooting dp. 全方位木DPの結果

    ex: simple. ただし累積和を使わない実装はうまく行かない問題。 https://atcoder.jp/contests/dp/tasks/dp_v
        N, MOD = R()
        XY = [R1() for _ in range(N-1)]

        children, topo_sort, parent, partial_size = topological_sorted_tree(XY, N)
        dp = retooting(
                children, topo_sort, parent, N, unit=1, 
                merge = lambda a, b: a * b % MOD, 
                adj_bu = lambda a, i: a + 1, 
                adj_td = lambda a, i, p: a + 1, 
                adj_fin = lambda a, i: a
            )
        print(*dp)

    ex2: 頂点更新時に子の数が必要な場合 https://atcoder.jp/contests/abc160/tasks/abc160_f
        (ほぼ同じ問題として https://atcoder.jp/contests/tdpc/tasks/tdpc_tree)
        N = r_int()
        XY = [R1() for _ in range(N-1)]
        MOD = 10**9+7

        children, topo_sort, parent, partial_size = topological_sorted_tree(XY, N)
        comb = ModComb(N, MOD)

        # ダメなパターンが何割含まれるか、をDPで積み重ねていき、最後に階乗を加えることで、全部の組合せを出す。かなり頭が混乱しますね。
        # 例えば1-2, 2-3, 2-4, 2-5, 2-6のN=6の木で、2の部分での更新に注目するとき、2の下の部分の並べ方のうち、良いパターンは2が先頭に来て、5-6の順序が整っていることである。「5-6の順序が整っていること」は5の部分の更新ですでに見ているため、あたらに考慮すべき部分は1/5を掛けることである。それがadj_buである。
        # dpを積み重ねていくことで、全通り中の良いパターンの確率ができており、それに全通り（Nの階乗）をかけてあげることで、組合せ総数が出てくる。
        
        dp = retooting(
                children, topo_sort, parent, N, unit=1, 
                merge = lambda a, b: a * b % MOD,
                adj_bu = lambda a, i: a * comb.inv(partial_size[i]) % MOD,
                adj_td = lambda a, i, p: a * comb.inv(N-partial_size[i]) % MOD,
                adj_fin = lambda a, i: a * comb.fact[N-1] % MOD
            )

        print(*dp)

    ex3: 木の最長距離（直径） https://atcoder.jp/contests/arc022/tasks/arc022_3
        N = r_int()
        XY = [R1() for _ in range(N-1)]
        children, topo_sort, parent, partial_size = topological_sorted_tree(XY, N)
        dp = retooting(
                children, topo_sort, parent, N, unit=0, 
                merge = lambda a, b: max(a,b),
                adj_bu = lambda a, i: a + 1,
                adj_td = lambda a, i, p: a + 1,
                adj_fin = lambda a, i: a
            )

        mdp = max(dp)
        ans = []

        for i, d in enumerate(dp):
            if d == mdp:
                ans.append(i+1)
                break
        
        edges = [list() for _ in range(N)]
        for x, y in XY:
            edges[x].append(y)
            edges[y].append(x)
        arrived = [0]*N
        arrived[i] = 1
        tasks = deque([i])
        while tasks:
            task = tasks.popleft()
            for node in edges[task]:
                if not arrived[node]:
                    arrived[node] = 1
                    tasks.append(node)
        ans.append(task+1)
        print(*ans)
        
    """

    # Bottom-Up 部分
    ACC = [unit] * N  # acc[i](=頂点iのp方向以外からの(=葉方向からの)集約(調整前))
    res_BU = [0] * N  #  res_BU[i], acc[i]に調整を入れたもの
    for i in Topo[:0:-1]:  # root=0部分はここでは計算しない
        p = P[i]  # 親ノード
        res_BU[i] = adj_bu(ACC[i], i)  # bottom up関数で res_BU[i]を作成
        ACC[p] = merge(ACC[p], res_BU[i])  # 親の集約
    res_BU[Topo[0]] = adj_fin(ACC[Topo[0]], Topo[0])

    res = [i for i in res_BU]

    # Top-Down 部分
    AL = [unit] * N  # accum from left
    TD = [unit] * N  # 根方向の合計
    for i in Topo:
        # 左からDP（結果はALに格納）
        ac = TD[i]  # ac: accum, 親を含めて左から累積merge
        for j in X[i]:
            AL[j] = ac
            ac = merge(ac, res_BU[j])
        # 右からDP（結果はacに入れており、右からのDP）
        ac = unit  # 右側は親を含めないので、左と合わせることで対象とするi以外の累積が取れる。
        for j in X[i][::-1]:
            TD[j] = adj_td(merge(AL[j], ac), j, i)  # jに根方向合計を格納
            ac = merge(ac, res_BU[j])  # ac（右からのDP）を更新
            res[j] = adj_fin(merge(ACC[j], TD[j]), j)

    return res


# ************ 文字列検索 ************
class KMP:
    """文字列Sから文字列Tを検索する手法。一致先頭のindexを返す。
    別にクラスにしなくてよかったという説がある。
    ref: https://ikatakos.com/pot/programming_algorithm/string_search
    ref: https://atcoder.jp/contests/abc150/tasks/abc150_f
    >>> kmp = KMP("すごいはすけるすごいすごい", "すごい")
    >>> print(kmp.L)
    [0, 7, 10]
    >>> kmp = KMP("abcaabcabcaabcdbabcdbabcabcaabcdbabc", "abcaabcdbabc")
    >>> print(kmp.L)
    [7, 24]
    """
    def __init__(self, S: str, T: str):
        self.S = S
        self.T = T
        self.L = self.kmp()

    def make_kmp_table(self, t):
        i = 2
        j = 0
        m = len(t)
        tbl = [0] * (m + 1)
        tbl[0] = -1
        while i <= m:
            if t[i - 1] == t[j]:
                tbl[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = tbl[j]
            else:
                tbl[i] = 0
                i += 1
        return tbl

    def kmp(self):
        matched_indices = []
        tbl = self.make_kmp_table(self.T)
        i = 0
        j = 0
        n = len(self.S)
        m = len(self.T)
        while i + j < n:
            if self.T[j] == self.S[i + j]:
                j += 1
                if j == m:
                    matched_indices.append(i)
                    i += j - tbl[j]
                    j = tbl[j]
            else:
                i += j - tbl[j]
                if j > 0:
                    j = tbl[j]
        return matched_indices


# KMPのほうが良さそう？
import random


def rabin_karp_Rolling_Hash(s, t):
    """
    https://ikatakos.com/pot/programming_algorithm/string_search
    ハッシュ化にO(|S|+|T|), 検索にO(S)
    >>> print(rabin_karp_Rolling_Hash("スパゲティスパゲッティ", "スパゲ"))
    [0, 5]
    """
    def exe(x, m):
        th = 0
        for c in tt:
            th = (th * x + c) % m

        sh = 0
        for c in st[:l]:
            sh = (sh * x + c) % m
        xl = pow(x, l - 1, m)

        matched = set()
        if sh == th:
            matched.add(0)
        for i, (c0, c1) in enumerate(zip(st, st[l:]), start=1):
            sh = ((sh - c0 * xl) * x + c1) % m
            if sh == th:
                matched.add(i)

        return matched

    l = len(t)
    st = list(map(ord, s))
    tt = list(map(ord, t))
    # Xはなるべくst,ttの最大要素より大きくする
    # Mはとりあえず2^61-1(素数)を設定する
    xs = random.sample(range(10**9, 10**10), 3)
    ans = exe(xs[0], 2305843009213693951)
    ans.intersection_update(exe(xs[1], 2305843009213693951))
    ans.intersection_update(exe(xs[2], 2305843009213693951))
    return sorted(ans)


def count_repetition(S):
    """count repetition in S(str or list): O(NlogN)と思う。思い付きで実装したので別に早くはない。O(N)ありそうだがNlogN十分でしょう。
    ref: https://atcoder.jp/contests/abc150/tasks/abc150_f

    Args:
        S (str or list): target

    Returns:
        int: cnt of repetition in S
    
    >>> print(count_repetition([1,1,2,1,1,2,1,1,2]))
    3
    >>> print(count_repetition("112112112"))
    3
    >>> print(count_repetition("abcbbabc"))
    1
    >>> print(count_repetition("abcabc"))
    2
    """
    for i in make_divisors(len(S)):
        if i == 1:
            repetition_S = 1
            continue
        for j in range(i):
            if S[:(len(S) // i)] != S[(len(S) // i) * j:(len(S) // i) *
                                      (j + 1)]:
                break
        else:
            repetition_S = i
    return repetition_S


def Zalgorithm(s):
    """
    O(n)で文字列Sの各開始位置iに対して「SとS[i:]が先頭何文字まで一致するか？
    （最長共通接頭辞数）」を構築するアルゴリズム。
    TODO: あまり理解はしていない。
    
    ref(実装): https://jetbead.hatenablog.com/entry/20130503/1367517589
    ref: https://ikatakos.com/pot/programming_algorithm/string_search
    >>> Zalgorithm("やばいやばかったやばいや")
    [12, 0, 0, 2, 0, 0, 0, 0, 4, 0, 0, 1]
    """
    ans = []
    ans.append(len(s))
    # ret = 0
    n = len(s)
    z = [0] * n
    L, R = 0, 0
    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and s[R - L] == s[R]:
                R += 1
            z[i] = R - L
            R -= 1
        else:
            k = i - L
            if z[k] < R - i + 1:
                z[i] = z[k]
            else:
                L = i
                while R < n and s[R - L] == s[R]:
                    R += 1
                z[i] = R - L
                R -= 1
        # ret = max(ret, z[i])
        ans.append(z[i])
    # return ret
    return ans


""" initialize variables and set inputs
# initialize variables
    # to initialize list, use [0] * n
    # to initialize two dimentional array:
        # ex) [[0] * N for _ in range(N)]
        # ex2) dp = [[0] * (N+1) for _ in range(W*2)]
# set inputs
    # put inputs between specific values (almost as quickly)
    # ex) S = [-INF] + [int(r()) for _ in range(A)] + [INF]
    # open(0).read() is sometimes useful:
    # ex) n, m, *x = map(int, open(0).read().split())
    #     min(x[::2]) - max(x[1::2])
    # ex2) *x, = map(int, open(0).read().split())
    #     don't forget to add comma after *x if only one variable is used
# preprocessing
    # transpose = [x for x in zip(*data)]
    # ex) [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    # flat = [flatten for inner in data for flatten in inner]
    # ex) [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # split: Point [〇 for _ in _ for _ in _]では左から順に評価されるが、[[〇 for _ in _] for _ in _]では外側から評価される
    # ex) KT = [[3, 1, 200, 1000], [5, 20, 30, 40, 50, 2]] K1, T11, T12, ...
    # K = [k for kt in KT for i, k in enumerate(kt) if i == 0]
    # T = [[k for i, k in enumerate(kt) if i != 0] for kt in KT]
    
# calculate and output
    # output pattern
    # ex1) print(*l) => when l = [2, 5, 6], printed 2 5 6
"""

# functions to read input
# TODO: なおsys.stdin.buffer.readline (read, readlines)のほうが多少早いことが多いらしい
# https://twitter.com/maspy_stars/status/1179226257982185472
r = lambda: sys.stdin.readline().strip()
rs = lambda N: [r() for _ in range(N)]
r_int = lambda: int(r())
r1_int = lambda: int(r()) - 1
r_float = lambda: float(r())
r_ints = lambda N: [r_int() for _ in range(N)]
r1_ints = lambda N: [r1_int() for _ in range(N)]

R = lambda: list(map(int, r().split()))
R_mod = lambda: list(map(ModInt, map(int, r().split())))
R1 = lambda: list(map(lambda x: int(x) - 1, r().split()))  # a,b = a-1,b-1の省略
Rs = lambda N: [R() for _ in range(N)]
R1s = lambda N: [R1() for _ in range(N)]
R1s_XYD = lambda N: [[x - 1, y - 1, z] for x, y, z in iter(
    R() for _ in range(N))]  # x, y, dでx,yだけ-1したい場合
R1s_S = lambda N, S, add=-1: [[
    x + add if i in set(S) else x for i, x in enumerate(R())
] for _ in range(N)]

R_str = lambda: list(r().split())
R1_S = lambda S, add=-1: [
    x + add if i in set(S) else x for i, x in enumerate(R())
]

R_map = lambda: map(int, r().split())
R_float = lambda: list(map(float, r().split()))


# R_tuple = lambda: tuple(map(int, r().split())) # not recommended because tuple looks slow in pypy(?)
def x10(S: str, n: int):
    """change float to int by *10**n

    Args:
        S (str): float
        n (int, optional): n of float(S)*10**n (number of shift).

    Returns:
        int: S*10**n
    """
    if "." not in S:
        return int(S) * 10**n
    return int("".join([S.replace(".", ""), "0" * (n - S[::-1].find("."))]))


Rx10 = lambda n: list(map(lambda s: x10(s, n), r().split()))

list2d = lambda a, b, v: [[v] * b for _ in range(a)]
list2d_mod = lambda a, b, v: [[ModInt(v) for _ in range(b)] for _ in range(a)]
list3d = lambda a, b, c, v: [[[v] * c for _ in range(b)]
                             for _ in range(a)]  # slow.
list3d_mod = lambda a, b, c, v: [[[ModInt(v) for _ in range(c)]
                                  for _ in range(b)]
                                 for _ in range(a)]  # slow.
list4d = lambda a, b, c, d, v: [[[[v] * d for _ in range(c)] for _ in range(b)]
                                for _ in range(a)]  # slow.
list4d_mod = lambda a, b, c, d, v: [[[[ModInt(v) for _ in range(d)]
                                      for _ in range(c)] for _ in range(b)]
                                    for _ in range(a)]  # slow.


class rr:
    r = lambda: sys.stdin.readline().strip()
    rs = lambda N: [rr.r() for _ in range(N)]
    r_int = lambda: int(rr.r())
    r1_int = lambda: int(rr.r()) - 1
    r_float = lambda: float(rr.r())
    r_ints = lambda N: [rr.r_int() for _ in range(N)]
    r1_ints = lambda N: [rr.r1_int() for _ in range(N)]

    R = lambda: list(map(int, rr.r().split()))
    R1 = lambda: list(map(lambda x: int(x) - 1,
                          rr.r().split()))  # a,b = a-1,b-1の省略
    Rs = lambda N: [rr.R() for _ in range(N)]
    R1s = lambda N: [rr.R1() for _ in range(N)]
    R1s_XYD = lambda N: [[x - 1, y - 1, z] for x, y, z in iter(
        rr.R() for _ in range(N))]  # x, y, dでx,yだけ-1したい場合
    R1s_S = lambda N, S, add=-1: [[
        x + add if i in set(S) else x for i, x in enumerate(rr.R())
    ] for _ in range(N)]

    R_str = lambda: list(rr.r().split())
    R1_S = lambda S, add=-1: [
        x + add if i in set(S) else x for i, x in enumerate(rr.R())
    ]

    R_map = lambda: map(int, rr.r().split())
    R_float = lambda: list(map(float, rr.r().split()))
    # R_tuple = lambda: tuple(map(int, rr.r().split())) # not recommended because tuple looks slow in pypy(?)
    @classmethod
    def x10(cls, S: str, n: int):
        """change float to int by *10**n

        Args:
            S (str): float
            n (int, optional): n of float(S)*10**n (number of shift).

        Returns:
            int: S*10**n
        """
        if "." not in S:
            return int(S) * 10**n
        return int("".join([S.replace(".", ""),
                            "0" * (n - S[::-1].find("."))]))

    Rx10 = lambda n: list(map(lambda s: rr.x10(s, n), rr.r().split()))


class List3d:
    def __init__(self, a, b, c, v):
        self.L = [v] * (a * b * c)
        self.a = a
        self.b = b
        self.c = c
        self.mul_a = b * c
        self.mul_b = c

    def update(self, a, b, c, v):
        self.L[a * self.mul_a + b * self.mul_b + c] = v

    def query(self, a, b, c):
        return self.L[a * self.mul_a + b * self.mul_b + c]


class List2d:
    def __init__(self, a, b, v):
        self.L = [v] * (a * b)
        self.a = a
        self.b = b
        self.mul_a = b

    def update(self, a, b, v):
        self.L[a * self.mul_a + b] = v

    def query(self, a, b):
        return self.L[a * self.mul_a + b]


def main(sample_file=''):
    """ how to treat input
    # single int: int(r())
    # single string: r()
    # single float: float(r())
    # line int: R()
    # line string: r().split()
    # line (str, int, int): [j if i == 0 else int(j) for i, j in enumerate(r().split())]
    # lines int: [R() for _ in range(n)]
    """

    # import numpy as np
    # for test
    if sample_file:
        sys.stdin = open(sample_file)

    # for creating random input
    import random

    # 問題の解き方
    # https://kimiyuki.net/blog/2016/06/21/how-to-solve-problems-in-competitive-programming/
    # https://algo-logic.info/how-to-think-cp/

    # 7で割れるか
    # a//10-(a%10)*2

    # OEIS
    # https://oeis.org/
    # https://kabukimining.hateblo.jp/entry/atcoder-OEIS

    # ----------------------------------
    # main

    # initialize
    ans = 1
    cnt = 0
    # pypyでdictに(a, b, c)みたいなの使うとTLE
    # https://atcoder.jp/contests/arc111/tasks/arc111_c

    # 考察コメント
    #

    # 犯罪/マラソン用
    # import time
    # time_sta = time.time()
    # a = time.time()-time_sta
    # if a > 1.8:
    #     print(-1)
    #     return

    N, Q = R()
    AB = R1s(N - 1)
    CD = R1s(Q)

    edges = [list() for _ in range(N)]
    for a, b in AB:
        edges[a].append(b)
        edges[b].append(a)
    depth = [-1] * N
    tasks = [[0, 0]]
    arrived = [0] * N
    while tasks:
        node, dep = tasks.pop()
        arrived[node] = 1
        depth[node] = dep
        dep += 1
        for next_node in edges[node]:
            if arrived[next_node]:
                continue
            tasks.append([next_node, dep])
    for c, d in CD:
        YesNo((depth[c] + depth[d]) % 2 == 0, "Town", "Road")

    #%%
    # end of main
    # ----------------------------------
    """memo: how to solve bit problems
    ref: https://primenumber.hatenadiary.jp/entry/2016/12/01/000000
    ビット列による部分集合表現 【ビット演算テクニック Advent Calendar 2016 1日目】
    
    https://atcoder.jp/contests/abc173/submissions/14966961
    for i in range(1<<h):
	    if (i >> x) & 1:
            hoge
    (i >> x) & 1 でxビット目のビット値を取得している

    https://atcoder.jp/contests/abc187/submissions/19255179
    i=110100110 のとき、j=110100110, 110100100, 110100010, ...を出力する方法
    for i in range(1<<N): # 各Sについて
        j = i
        while j:
            if dp[i] > dp[j] + dp[i^j]:
                dp[i] = dp[j] + dp[i^j]
            j -= 1 # これにより、例えばi=110100110のとき、j =110100101
            j &= i # これにより、j = 110100100となり、一番下に立っている1を消去できた
            
    bitDPで間違いやすいのが、for i in range(N)としてiを作成した際、集合Sとの和集合をとる際に[S|(1<<i)]とすべきところ[S|i]としやすいことと、print(dp[(1<<N)-1][0])とすべきところ、print(dp[1<<N-1][0]などと書きやすいこと。<<は計算順序的に遅いので、しっかり括弧を付けて優先的に計算されるように明示する。
    ex: https://atcoder.jp/contests/abc180/submissions/19837195
        dp = list2d(1<<N, N, INF) # 集合Sについて到着し, 開始地点がNで最後に0に到着する最短経路
        for i in range(N):
            dp[1<<i][i] = dist[i][0]
        for S in range(1<<N):
            for i in range(N): # 新しく追加する開始地点
                if (S>>i) & 1:
                    continue
                for j in range(N): # 追加前の開始地点
                    if (S>>j) & 1 == 0:
                        continue
                    dp[S|(1<<i)][i] = min(dp[S|(1<<i)][i], dp[S][j]+dist[i][j])    
        print(dp[(1<<N)-1][0])
    """


if __name__ == '__main__':
    main()
    # print('*** doctest start ***')
    # import doctest
    # doctest.testmod()
    # print('*** doctest end ***')
