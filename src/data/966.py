import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(2000000000)

n, q = map(int, input().split(" "))

graph = defaultdict(lambda: [])
for i in range(n - 1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

costs = [None for i in range(n + 1)]


def f(jibun, oya, jibun_key):
    kids = graph[jibun]
    costs[jibun] = jibun_key

    #kid_id = 0
    #kid_key = jibun_key + 1
    kid_key = not jibun_key
    for kid in kids:
        if kid == oya:
            continue
        f(kid, jibun, kid_key)


def calc_dist(key1, key2):
    len1 = key1
    len2 = key2
    ret = (len1 - len2) % 2
    return ret


#f(1, None, (0,))
#f(1, None, 0)
f(1, None, False)
#print(costs)

for i in range(q):
    c, d = map(int, input().split(" "))
    key_c = costs[c]
    key_d = costs[d]
    dist = calc_dist(key_c, key_d)
    if dist == 0:
        out = "Town"
    else:
        out = "Road"
    print(out)
