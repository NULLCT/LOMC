from sys import stdin

read = stdin.readline
(N, Q) = map(int, read().split())
AB = [list(map(lambda i: int(i) - 1, read().split())) for j in range(N - 1)]
CD = [list(map(lambda i: int(i) - 1, read().split())) for j in range(Q)]

nbr = [set() for i in range(N)]
for (a, b) in AB:
    nbr[a].add(b), nbr[b].add(a)

dtc = [None for i in range(N)]
q = [(0, 0)]
used = set()
while len(q) != 0:
    (i, d) = q.pop()
    used.add(i)
    dtc[i] = d
    for j in nbr[i]:
        if j in used:
            continue
        q.append((j, d + 1))

for (c, d) in CD:
    print("Town" if dtc[c] % 2 == dtc[d] % 2 else "Road")
