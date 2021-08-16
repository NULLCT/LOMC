import networkx as nx

N, Q, *l = map(int, open(0).read().split())
A = l[0:2 * (N - 1):2]
B = l[1:2 * (N - 1):2]
C = l[2 * (N - 1)::2]
D = l[2 * (N - 1) + 1::2]

G = nx.Graph()
G.add_nodes_from(range(1, N + 1))

edges = [(A[i], B[i]) for i in range(len(A))]
G.add_edges_from(edges)  # 一括で追加

length = nx.single_source_shortest_path_length(G, 1)
ans = [0] * Q
for i in range(Q):

    c = C[i]
    d = D[i]
    if (length[c] - length[d]) % 2 == 0:
        ans[i] = "Town"
    else:
        ans[i] = "Road"

print(*ans, sep='\n')
