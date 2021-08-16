from collections import defaultdict

n, q = list(map(int, input().split()))
d = defaultdict(set)
dc = dict()
for i in range(n - 1):
    ai, bi = list(map(int, input().split()))
    d[ai].add(bi)
    d[bi].add(ai)

toexplore = [(1, 0)]

for t in toexplore:
    x, i = t
    if x in dc:
        continue
    dc[x] = i
    toexplore += [(y, 1 - i) for y in d[x]]

for i in range(q):
    ci, di = list(map(int, input().split()))
    if dc[ci] != dc[di]:
        print('Road')
    else:
        print('Town')
