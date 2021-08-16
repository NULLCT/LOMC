import sys

sys.setrecursionlimit(10**6)

n, q = map(int, input().split())

R = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    R[a].append(b)
    R[b].append(a)

bw = [None] * (n + 1)


def func(_bw, _r, a, b):
    _bw[b] = not _bw[a]

    for e in _r[b]:
        if e == a:
            continue
        func(_bw, _r, b, e)


bw[1] = True
for b in R[1]:
    func(bw, R, 1, b)

for _ in range(q):
    c, d = map(int, input().split())

    if bw[c] == bw[d]:
        print("Town")
    else:
        print("Road")
