from sys import setrecursionlimit

setrecursionlimit(10**6)


def rec(now: int, depth: int = -1):
    if this_node_depth_is_odd[now] != -1:
        return this_node_depth_is_odd[now]
    this_node_depth_is_odd[now] = depth % 2
    for n_node in edge[now]:
        if this_node_depth_is_odd[n_node] != -1:
            continue
        rec(n_node, depth + 1)
    return


N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda n: int(n) - 1, input().split())
    edge[x].append(y)
    edge[y].append(x)  # 有向グラフならこの行は消す!!

this_node_depth_is_odd = [-1] * N
rec(0)

for _ in range(Q):
    c, d = map(lambda a: int(a) - 1, input().split())
    if this_node_depth_is_odd[c] == this_node_depth_is_odd[d]:
        print("Town")
    else:
        print("Road")
