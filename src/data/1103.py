import sys

sys.setrecursionlimit(10**8)

n, q = map(int, input().split())
p = {}
for i in range(n - 1):
    a, b = map(int, input().split())
    if a in p:
        p[a].add(b)
    else:
        p[a] = set([b])
    if b in p:
        p[b].add(a)
    else:
        p[b] = set([a])
town = [0] * (n + 1)


def aaa(k):
    for l in p[k]:
        if town[l] == 0:
            town[l] = 3 - town[k]
            aaa(l)


town[1] = 1
aaa(1)
for j in range(q):
    a, b = map(int, input().split())
    if town[a] == town[b]:
        print("Town")
    else:
        print("Road")
