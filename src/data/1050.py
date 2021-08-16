import math, sys
#from itertools import permutations, combinations;import heapq,random;
from collections import defaultdict, deque
import bisect as bi


def yes():
    print('YES')


def no():
    print('NO')


#sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
def I():
    return (int(sys.stdin.readline()))


def In():
    return (map(int, sys.stdin.readline().split()))


def Sn():
    return sys.stdin.readline().strip()


#sys.setrecursionlimit(1500)
#import resource, sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

sys.setrecursionlimit(10**7)


def dict(a):
    d = {}
    for x in a:
        if d.get(x, -1) != -1:
            d[x] += 1
        else:
            d[x] = 1
    return d


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:
        return -1


def dfs(v, p, timer):
    timer[0] += 1
    tin[v] = timer[0]
    dp[v][0] = p
    for i in range(1, lo + 1):
        dp[v][i] = dp[dp[v][i - 1]][i - 1]
    cnt = 0
    for x in d[v]:
        if x != p:
            high[x] = high[v] + 1
            cnt += 1
            dfs(x, v, timer)
    timer[0] += 1
    tout[v] = timer[0]


def is_ancestor(u, v):
    return tin[u] <= tin[v] and tout[u] >= tout[v]


def lca(u, v):
    if is_ancestor(u, v):
        return u
    if is_ancestor(v, u):
        return v
    for i in range(lo, -1, -1):
        if not is_ancestor(dp[u][i], v):
            u = dp[u][i]
    return dp[u][0]


def main():
    try:
        global lo, n, ans, k, visit, d, dp, tin, tout, high, leaf_node
        n, nQ = In()
        visit = [False] * (n + 1)
        high = [-1] * (n + 1)
        tin = [-1] * (n + 1)
        tout = [-1] * (n + 1)
        d = defaultdict(list)

        for i in range(n - 1):
            a, b = In()
            d[a].append(b)
            d[b].append(a)
        timer = [0]

        lo = math.ceil(math.log(n, 2))
        dp = [[0 for i in range(lo + 1)] for j in range(n + 1)]
        high[1] = 0
        dfs(1, 1, timer)
        for i in range(nQ):
            v, u = In()
            z = lca(v, u)
            distance = high[u] - high[z] + high[v] - high[z]
            if distance % 2 == 0:
                print("Town")
            else:
                print("Road")
    except:
        pass


M = 998244353
P = 1000000007

if __name__ == '__main__':
    # for _ in range(I()):main()
    for _ in range(1):
        main()
#End#

#        ******************* All The Best *******************   #
