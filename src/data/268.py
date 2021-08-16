from collections import defaultdict, deque
from heapq import heappop, heappush
import math
import sys
import itertools
import bisect
#sys.setrecursionlimit(10**9)
#import numpy as np
import decimal

INF = float('inf')


class UnionFind():
    def __init__(self, n):
        # classのお気持ち
        self.n = n
        #0~n-1の要素がありすべての要素の親は-1
        self.parents = [-1] * n

    def find(self, x):
        #xがどこにいるかを探している
        #親だったら自分を子だったら親を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        #要素xとyを結合する
        #xとyの親を探す
        x = self.find(x)
        y = self.find(y)
        if x == y:
            #親が同じだったらそのまま
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        #xが含まれるunionのサイズ
        return -self.parents[self.find(x)]

    def same(self, x, y):
        #xとyが同じunionであるかの判定
        return self.find(x) == self.find(y)

    def members(self, x):
        #xが含まれるunionのメンバー
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        #親の集合
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        #unionの数
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}'
                         for r, m in self.all_group_members().items())


def comb(n, r, mod):
    if r < 0 or n < r:
        return 0
    N = n
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


def is_prime(n):
    #nが素数であるかの判定
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def primes(n):
    #nまでの素数列挙
    #リストのその番目が1だったら素数(0から)
    nums = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        nums.pop()
    nums[1] = 0
    nums[2] = 1
    for p in range(3, int(n**0.5) + 1, 2):
        if nums[p]:
            for q in range(p**2, n + 1, 2 * p):
                nums[q] = 0
    return nums


def soinsu(n):
    ans = []
    num = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if num % i == 0:
            coun = 0
            while num % i == 0:
                coun += 1
                num //= i
            ans.append([i, coun])
    if num != 1:
        ans.append([num, 1])
    if ans == []:
        ans.append([n, 1])
    return ans


def arr_pow(A, p, mod):
    res = np.eye(A.shape[0], dtype=np.int64)
    while p:
        if p & 1:
            res = np.dot(res, A) % mod
        A = np.dot(A, A) % mod
        p >>= 1
    return res


def dijk(n, road, start):
    #(町の数,道路のリスト,出発地点)
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0
    visit = [False for _ in range(n + 1)]
    hq = [(0, start)]  #(距離,場所)
    while hq:
        h = heappop(hq)
        dis = h[0]
        pla = h[1]
        if visit[pla]:
            continue
        visit[pla] = True
        for q in road[pla]:
            num = q[0]
            cost = q[1]
            if visit[num] == False:
                if dist[num] > dist[pla] + cost:
                    dist[num] = dist[pla] + cost
                    heappush(hq, (dist[pla] + cost, num))
    return dist


def arr_arr(A, B, mod):
    I, J, K = len(A), len(B[0]), len(B)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += A[i][k] * B[k][j]
            c[i][j] %= mod
    return c


def arr_pow(x, n, mod):
    #行列の累乗
    #x^n
    y = [[0] * len(x) for _ in range(len(x))]
    for i in range(len(x)):
        y[i][i] = 1
    while n > 0:
        if n & 1:
            y = arr_arr(x, y, mod)
        x = arr_arr(x, x, mod)
        n >>= 1
    return y


def w_f(N, road):
    #ワ―シャルフロイド法
    #(街の数、道路のリスト)
    dist = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for i in range(N):
        for k in road[i + 1]:
            dist[i][k[0] - 1] = min(k[1], dist[i][k[0] - 1])
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# ord('a') = 97 ord('z') = 122 ord('A') = 65 ord('Z') = 90

################################
#　　　目　　　　　　次　　　　　 #
################################

# class UnionFind
# find(x) xの親を返す(親だったら自分)
# union(x,y) xとyを結合する
# size(x) xが含まれるunionのサイズ
# same(x,y) xとyが同じかの判定
# members(x) xが含まれるunionのメンバー
# roots() 親の集合
# group_count() unionの数
# all_group_members　辞書型でunion全体を返す
#comb(n,r,mod) nCr (mod)
#is_prime(n) nが素数かの判定
#primes(n) nまでの整数列挙
#soinsu(n) nを素因数分解
#arr_pow(A, p, mod) 行列累乗
#dijk(n,road,start) ダイクストラn個の街road道のリストstart開始位置
#arr_arr(A,B,mod) 行列A*B
#w_f(N,road) ワ―シャルフロイド法

#################################
# ここからコードが始まったりする #
#################################

N, Q = map(int, input().split())
road = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)
dist = [-1 for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
dist[1] = 1
d = deque([1])
while d:
    q = d.popleft()
    visit[q] = True
    p = dist[q]
    for num in road[q]:
        if visit[num]:
            continue
        dist[num] = (p + 1) % 2
        d.append(num)
for _ in range(Q):
    c, d = map(int, input().split())
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
