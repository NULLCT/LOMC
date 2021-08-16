import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

even_or_odd = [False for _ in range(N)]
# even => 0
used = set()
node = 0


def func(node, even):
    global E
    global even_or_odd
    global used
    for node2 in E[node]:
        if node2 in used:
            continue
        else:
            used.add(node2)
            even_or_odd[node2] = not even
            func(node2, not even)


func(0, True)

ans = []
for q in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if even_or_odd[c] == even_or_odd[d]:
        ans.append("Town")
    else:
        ans.append("Road")

for s in ans:
    print(s)
"""
INF = 10 ** 10

N, X = map(int, input().split())
A = (map(int, input().split()))
for idx, a in enumerate(A):
    if idx % 2 == 0:
        X -= a
    else:
        X -= a - 1
    if X < 0:
        exit(print("No"))
print("Yes")
"""
