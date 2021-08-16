def bfs() -> list:
    # Data Structure for graph search
    vertices_num = len(a_graph)  # Number of vertices the graph has
    seen = [False] * vertices_num  # All vertices are not "seen" yet,
    seen[0] = 0  # but only vertex-s (root of tree) is "seen"
    todo = [0]  # Only vertex-s (root of tree) is in "todo"
    depth = 0  # Variable to count depth of tree

    # Continue searching until "todo" becomes empty
    while todo:
        depth += 1
        todo_tmp = []
        # Pull out a vertex from the head of "todo"
        for i in todo:
            # Search all "not-seen" vertices adjacent to vertex-i
            for j in a_graph[i]:
                # Do nothing if vertex-j is already "seen"
                if seen[j]:
                    continue

                # Make vertex-j "seen", and append it into "todo_tmp"
                seen[j] = depth
                todo_tmp.append(j)

        todo = todo_tmp

    return seen


def create_graph(edge_num: int, edge_list: list) -> dict:
    """
    Create a graph expressed with adjacency list
    :dict_key    : int (a vertex)
    :dict_value  : set (consisted of vertices adjacent to key vertex)
    """
    a_graph = {i: set() for i in range(edge_num)}

    for a, b in edge_list:
        a_graph[a - 1].add(b - 1)  # All graphs always need this line
        a_graph[b - 1].add(a - 1)  # Only undirected graph needs this line

    return a_graph


N, Q = map(int, input().split())
LL1 = [list(map(int, input().split())) for _ in range(N - 1)]
LL2 = [list(map(int, input().split())) for _ in range(Q)]

a_graph = create_graph(N, LL1)
a_list = bfs()
for c, d in LL2:
    res = 'Town' if (a_list[c - 1] + a_list[d - 1]) % 2 == 0 else 'Road'
    print(res)
