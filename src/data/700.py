import math
import copy
from collections import deque
# from typing import Collection, List, OrderedDict
# from union_find import UnionFind
import sys

# https://techblog.nhn-techorus.com/archives/15289 より 中央値の高速算出アルゴリズム


def partition(lst, pivot):
    """Modifired partition algorithm in section 7.1"""
    pivot_idx = None
    for idx, value in enumerate(lst):
        if value == pivot:
            pivot_idx = idx
    if pivot_idx is None:
        raise Exception
    lst[pivot_idx], lst[-1] = lst[-1], lst[pivot_idx]
    pivot = lst[-1]
    i = -1
    for j, val in enumerate(lst[:-1]):
        if val <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[-1] = lst[-1], lst[i + 1]
    return i + 1


def select(lst, i):
    """Selection in linear time"""
    if len(lst) == 1:
        return lst[0]
    split_lists = [lst[i * 5:(i + 1) * 5] for i in range((len(lst) + 4) // 5)]
    split_list_medians = [
        sorted(split_list)[(len(split_list) - 1) // 2]
        for split_list in split_lists
    ]
    x = select(split_list_medians, (len(split_list_medians) - 1) // 2)
    k = partition(lst, x)
    if i == k:
        return x
    elif i < k:
        return select(lst[:k], i)
    else:
        return select(lst[k + 1:], i - (k + 1))


def median_linear(lst):
    """Calculate median by selection algorithm"""
    return select(lst, (len(lst) - 1) // 2)


# nCrを求める https://qiita.com/Ma_AtoP/items/b9070518ff6e207e64a8
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# https://qiita.com/keisuke-ota/items/6c1b4846b82f548b5dec より
class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = -1  # 未探索の場合は -1 を返す。探索済みの場合、

    def __repr__(self):
        return f'Node index:{self.index} nears:{self.nears} sign:{self.sign}'


# 緩和
def chmin(a, b):
    if a > b:
        a = b  # 参照渡し
        return True
    else:
        return False


# 距離を返す


def bfs(nodes, start):

    # BGS
    queue = deque()
    # 本問では node start から探索を開始するため queue に node[start]  を最初に入れる
    nodes[start].sign = 0  # スタートの距離を0とする
    queue.append(nodes[start])

    # queue がなくなるまで探索を続ける
    while queue:
        # queue から node を 1 つ取り出す。取り出したノードについて調べる。
        # 取り出された node は queue から消える。
        node = queue.popleft()  # .pop() にすると DFS になる
        # 取り出された node の隣接 node 達を nears に入れる。
        nears = node.nears

        # 隣接 node 達が探索済みか 1 つずつ調べる。
        for near in nears:
            # 未探索の隣接 node は queue に追加する。
            # 取り出してきた親 node は道しるべとなるため、子 node の sign メソッドに追加する。
            if nodes[near].sign == -1:
                queue.append(nodes[near])
                nodes[near].sign = node.sign + 1  # ノードの隣は距離を1個増やす

    return


def main():
    # N = int(input())
    N, Q = map(int, input().split())

    links = [list(map(int, input().split())) for _ in range(N - 1)]
    que = [list(map(int, input().split())) for _ in range(Q)]

    # print(que)

    nodes = []
    # 町
    for i in range(N + 1):
        nodes.append(Node(i))

    # 道
    for j in range(N - 1):
        edge_start, edge_end = links[j]
        nodes[edge_start].nears.append(edge_end)
        nodes[edge_end].nears.append(edge_start)  # 有向グラフの場合は消す

    bfs(nodes, 1)

    for q in que:
        # print(q)
        start, end = q
        if abs(nodes[start].sign - nodes[end].sign) % 2:
            # 距離差が奇数のときは路上、偶数のときは町
            print("Road")
        else:
            print("Town")

            # G = [-1] * M
            # B = [-1] * M
            # C = [-1] * M

            # for m in range(M):
            #     A[m], B[m], C[m] = map(int, input().split())
            #     G[m] = []
            #     G[m].append(Edge(B[m], C[m]))

            # # A = list(map(int, input().split()))
            # # B = list(map(int, input().split()))
            # # C = list(map(int, input().split()))

            # print(G)
            # print(dijkstra(A[0], B[0], N, G))


if __name__ == "__main__":
    main()
