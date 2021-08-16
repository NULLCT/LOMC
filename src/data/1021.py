def bipartite(E):
    '''
    Input:
    E: the adjacency list of the graph
    Output:
    If the graph is bipartite, return [[U_1, U_2] (the parts of the bipartite graph) for each component].
    Else, return None.
    '''
    N = len(E)
    color = [None] * N
    part = []
    for x in range(N):
        if color[x] is not None: continue
        stack = [(x, 0)]  # color x with 0
        parts = [[], []]
        while stack:
            v, c = stack.pop()
            if color[v] is not None:  # consistent
                continue
            color[v] = c
            parts[c].append(v)
            for u in E[v]:
                if color[u] is None:  # not visited yet
                    stack.append(
                        (u,
                         c ^ 1))  # paint u with different color from v's one
                elif color[u] != c:  # consistent
                    continue
                else:  # inconsistent
                    return None
        part.append(parts)
    return part


N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    E[a].append(b)
    E[b].append(a)

color = [None] * N
stack = [(0, 0)]
parts = [[], []]
while stack:
    v, c = stack.pop()
    if color[v] is not None:  # consistent
        continue
    color[v] = c
    parts[c].append(v)
    for u in E[v]:
        if color[u] is None:  # not visited yet
            stack.append(
                (u, c ^ 1))  # paint u with different color from v's one

U1, U2 = parts
U1, U2 = set(U1), set(U2)

for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (c in U1 and d in U1) or (c in U2 and d in U2):
        print('Town')
    else:
        print('Road')
