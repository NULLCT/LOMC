from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n, q = [int(v) for v in input().split()]

edges_a = []
edges_b = []
for _ in range(n - 1):
    a, b = [int(v) for v in input().split()]
    edges_a.append(a - 1)
    edges_b.append(b - 1)
g = csr_matrix(([1] * (n - 1), (edges_a, edges_b)), shape=[n, n])

dist = [int(a + 1e-9) for a in dijkstra(csgraph=g, directed=False, indices=0)]

for _ in range(q):
    a, b = [int(v) for v in input().split()]
    if (dist[a - 1] + dist[b - 1]) % 2 == 0: print('Town')
    else: print('Road')
