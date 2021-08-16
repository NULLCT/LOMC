from os import environ
import sys
import math
from queue import Queue
if environ.get("hardik"):
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
print = sys.stdout.write
mod = (10**9) + 7


def I():
    return input()


def II():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


def P(z=''):
    print(str(z) + '\n')


def LP(z=[]):
    for i in z:
        print(str(i) + ' ')
    print('\n')


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def sieve(n):
    isPrimes = [True for i in range(n + 1)]
    isPrimes[0], isPrimes[1] = False, False
    p = 2
    while p * p <= n:
        if isPrimes[p] == True:
            for j in range(p * p, n, p):
                isPrimes[j] = False
        p += 1


n, queries = MI()
mat = [[] for x in range(n)]
for i in range(n - 1):
    a, b = MI()
    mat[a - 1].append(b - 1)
    mat[b - 1].append(a - 1)
colors = [None for _ in range(n)]
isVisited = [0 for _ in range(n)]
colors[0] = 0
q = Queue()
q.put(0)
while not q.empty():
    node = q.get()
    for i in mat[node]:
        if colors[i] == None:
            colors[i] = 1 - colors[node]
            q.put(i)
for i in range(queries):
    a, b = MI()
    a -= 1
    b -= 1
    if colors[a] == colors[b]:
        P("Town")
    else:
        P("Road")
