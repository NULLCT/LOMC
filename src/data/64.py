import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools
import time, random

sys.setrecursionlimit(10**6)

inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
df = collections.defaultdict


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def pf(s):
    return print(s, flush=True)


def pe(s):
    return print(str(s), file=sys.stderr)


def JA(a, sep):
    return sep.join(map(str, a))


def JAA(a, s, t):
    return s.join(t.join(map(str, b)) for b in a)


def main():
    n, q = LI()
    ab = [LI_() for _ in range(n - 1)]
    cd = [LI_() for _ in range(q)]

    e = df(set)
    for a, b in ab:
        e[a].add(b)
        e[b].add(a)

    def search(s):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv in e[u]:
                if v[uv]:
                    continue
                vd = k + 1
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    s = search(0)
    rr = []
    for c, d in cd:
        t = s[c] + s[d]
        if t % 2 == 1:
            rr.append("Road")
        else:
            rr.append("Town")

    return JA(rr, "\n")


# start = time.time()
print(main())
# pe(time.time() - start)
