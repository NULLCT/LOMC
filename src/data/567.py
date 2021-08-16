def Is():
    return input()


def Iss():
    return input().split()


def Ii():
    return int(input())


def Iis():
    return map(int, input().split())


def Iil():
    return list(map(int, input().split()))


def Ixy(N):
    return [list(map(int, input().split())) for l in range(N)]


def Ixyind(N):
    xy = [map(int, input().split()) for _ in range(N)]
    return [list(i) for i in zip(*xy)]


def Imixind(N):
    list = []
    for i in range(N):
        a, b = input().split()
        list.append([int(a), b])
    return list


#####################################################################
import sys

sys.setrecursionlimit(100000)


def main():
    # N = Ii()
    # S = Is()
    N, Q = Iis()

    # l = Iil()
    # X,Y = Ixyind(N)
    # XY = Ixy(N)

    class Node:
        def __init__(self):
            self.parents = []
            self.children = []
            self.depth = None

    def cal_depth(node_id, d=0):
        Tree[node_id].depth = d
        for child in Tree[node_id].children:
            if Tree[child].depth == None:
                cal_depth(child, d + 1)
        for parent in Tree[node_id].parents:
            if Tree[parent].depth == None:
                cal_depth(parent, d - 1)

    Tree = [Node() for _ in range(N)]

    for i in range(N - 1):
        #id, 子供の数k, c_0~c_k
        tree_info = list(map(int, input().split()))
        node_id = tree_info[0] - 1
        k = 1

        if k > 0:
            children = tree_info[1] - 1
            Tree[node_id].children.append(children)
            Tree[node_id].type = "internal node"
        else:
            Tree[node_id].type = "leaf"

        for child in Tree[node_id].children:
            Tree[child].parents.append(node_id)

    #search_root
    root_id = [i for i, t in enumerate(Tree) if t.parents == []][0]
    Tree[root_id].type = "root"
    cal_depth(root_id)

    # answer_output
    # for i, t in enumerate(Tree):
    #     print("node {}: parents = {}, depth = {}, {}".format(i, t.parents, t.depth, t.children))
    for _ in range(Q):
        c, d = Iis()
        c -= 1
        d -= 1
        if Tree[c].depth % 2 == Tree[d].depth % 2:
            print("Town")
        else:
            print("Road")


main()
