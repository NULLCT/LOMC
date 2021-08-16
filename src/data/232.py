import sys, math
from collections import deque, defaultdict
import operator as op
from functools import reduce
from itertools import permutations
import heapq

# sys.setrecursionlimit(10**6)
# OneDrive\Documents\codeforces

I = sys.stdin.readline

alpha = "abcdefghijklmnopqrstuvwxyz"

mod = 10**9 + 7
"""
x_move=[-1,0,1,0,-1,1,1,-1]
y_move=[0,1,0,-1,1,1,-1,-1]
"""


def ii():
    return int(I().strip())


def li():
    return list(map(int, I().strip().split()))


def mi():
    return map(int, I().strip().split())


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def isPrime(n):
    if n <= 1:
        return False
    elif n <= 2:
        return True
    else:

        for i in range(2, int(n**.5) + 1):
            if n % i == 0:
                return False
        return True


def main():
    ans = ""
    n, num_of_queries = mi()
    d = defaultdict(list)
    for i in range(n - 1):
        u, v = mi()
        d[u].append(v)
        d[v].append(u)
    tmp = []
    for q in range(num_of_queries):
        u, v = mi()
        tmp.append((u, v))

    vis = [-1] * (n + 1)

    q = deque([(1, 0)])

    vis[1] = 0

    while q:
        x = q.popleft()
        for i in d[x[0]]:
            if vis[i] == -1:
                q.append((i, x[1] + 1))
                vis[i] = x[1] + 1

    for q in tmp:
        if abs(vis[q[0]] - vis[q[1]]) % 2:
            ans += "Road\n"
        else:
            ans += "Town\n"
    print(ans)


if __name__ == '__main__':
    main()
