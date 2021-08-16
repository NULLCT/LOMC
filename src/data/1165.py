#from itertools import product
#from itertools import combinations
#from collections import Counter
#from collections import defaultdict
#from collections import deque # deque([iterable[, maxlen]])
#from heapq import heapify, heappop, heappush # func(heapifiedlist, item)
# sadness lies below
#from bisect import bisect_left, bisect_right, insort # func(sortedlist, item)
#from sys import setrecursionlimit

from sys import stdin, stderr

input = stdin.readline


def dbp(*args, **kwargs):  # calling with dbp(locals()) is perfectly cromulent
    pass  # print(*args, file=stderr, **kwargs)


def get_int_list():
    return [int(x) for x in input().strip().split()]


def do_thing():
    N, Q = get_int_list()
    g = [[] for v in range(N)]
    for r in range(N - 1):
        a, b = get_int_list()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    dbp(g)
    rbv = [None] * N
    q = [(0, True)]
    while q:
        v, rb = q.pop()
        if rbv[v] != None:
            continue
        rbv[v] = rb
        for cv in g[v]:
            if rbv[cv] == None:
                q.append((cv, not rb))
    dbp(rbv)

    outl = []
    for q in range(Q):
        c, d = get_int_list()
        dbp(c - 1, d - 1, rbv[c - 1], rbv[d - 1])
        if rbv[c - 1] != rbv[d - 1]:
            outl.append('Road')
        else:
            outl.append('Town')

    return '\n'.join(outl)


def multicase():
    maxcc = int(input().strip())
    for cc in range(maxcc):
        print(do_thing())


if __name__ == "__main__":
    #multicase()
    print(do_thing())
