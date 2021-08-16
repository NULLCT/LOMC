import sys  #追加

sys.setrecursionlimit(100000000)  #追加


class Node:
    def __init__(self, id, len_to_root):
        self.id = id
        self.len_to_root = len_to_root


def main():
    N, Q = map(int, input().split())

    routes = [set() for _ in range(N)]

    for i in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        routes[a].add(b)
        routes[b].add(a)

    node_hash = [None] * N

    def generate_tree(node, parent_id):
        id = node.id
        next_len = node.len_to_root + 1

        for dst in routes[id]:
            if dst == parent_id:
                continue

            child = Node(dst, next_len)
            node_hash[dst] = child

            generate_tree(child, id)

    root = Node(0, 0)
    node_hash[0] = root
    generate_tree(root, -1)

    for _ in range(Q):
        c, d = map(lambda x: int(x) - 1, input().split())

        node_c = node_hash[c]
        node_d = node_hash[d]

        c_len = node_c.len_to_root
        d_len = node_d.len_to_root

        print("Town" if (c_len - d_len) % 2 == 0 else "Road")


main()
