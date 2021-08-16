from collections import deque

N, Q = map(int, input().split())
adjacencies = {vertex: [] for vertex in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    adjacencies[a].append(b)
    adjacencies[b].append(a)
root = 1
distance = {root: 0}
queue = deque([root])
while queue:
    vertex = queue.popleft()
    for adj_vertex in adjacencies[vertex]:
        if adj_vertex not in distance:
            distance[adj_vertex] = distance[vertex] + 1
            queue.append(adj_vertex)
ans_list = []
for _ in range(Q):
    c, d = map(int, input().split())
    if abs(distance[c] - distance[d]) % 2 == 0:
        ans_list.append('Town')
    else:
        ans_list.append('Road')
for a in ans_list:
    print(a)
