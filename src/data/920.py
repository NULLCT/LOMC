import collections

N, Q = map(int, input().split())
pathes = collections.defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    pathes[a].append(b)
    pathes[b].append(a)
parent = dict()
seen = set()
root = 1
que = set([root])
d = 0
depth = dict()
while (que):
    buff = set()
    for p in que:
        if (p in seen):
            continue
        seen.add(p)
        depth[p] = d
        for ch in pathes[p]:
            if (not ch in seen):
                buff.add(ch)
    d += 1
    que = buff
for i in range(Q):
    c, d = map(int, input().split())
    ans = "Town" if (depth[c] + depth[d]) % 2 == 0 else "Road"
    print(ans)
