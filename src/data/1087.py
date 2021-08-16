N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
cd = [list(map(int, input().split())) for _ in range(Q)]

edges = [set() for _ in range(N)]
for a, b in ab:
    edges[a - 1].add(b - 1)
    edges[b - 1].add(a - 1)

stack = [(True, 0)]
reached = [False] * N
reached[0] = True
evens = [True] * N
while stack:
    even, city = stack.pop()
    evens[city] = even
    for to in edges[city]:
        if reached[to]:
            continue
        reached[to] = True
        stack.append((not even, to))

for c, d in cd:
    if (evens[c - 1] + evens[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
