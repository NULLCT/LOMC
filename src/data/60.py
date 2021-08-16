def bfs(s: int) -> None:
    """
    :param s:
        start vertex.
    :variable vertices_num:
        number of vertices the graph has.
    :variable seen:
        memoitize each vertex is already seen or not.
            - initial value (-1)          : means "not seen yet".
            - updated value (zero or more): means "already seen" and its value is the vertex's depth from the root.
    :variable todo:
        vetices adjacent to the vertex in todo will be searched.
    :variable depth:
        the depth at that time.
    """

    # Data Structure for graph search
    vertices_num = len(a_graph)
    seen = [-1] * vertices_num
    seen[s] = 0
    todo = [s]
    depth = 0

    # Continue searching until "todo" becomes empty
    while todo:
        depth += 1
        todo_tmp = []
        # Pull out a vertex from the head of "todo"
        for i in todo:
            # Search all "not-seen" vertices adjacent to vertex-i
            for j in a_graph[i]:
                # Do nothing if vertex-j is already "seen"
                if seen[j] >= 0:
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
a_list = bfs(0)
for c, d in LL2:
    res = 'Town' if (a_list[c - 1] + a_list[d - 1]) % 2 == 0 else 'Road'
    print(res)
