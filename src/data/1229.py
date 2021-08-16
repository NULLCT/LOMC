# = int(input())
n, q = map(int, input().split())
# = list(map(int,input().split()))
# = [list(map(int,input().split())) for _ in range(N)]

connection_array = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    connection_array[a].append(b)
    connection_array[b].append(a)

zero_one = [0 for _ in range(n)]

now_node = [0]
zero_one[0] = 1
now_number = 1

while len(now_node) != 0:
    improve_node_array = []
    for node_ in now_node:
        for candidate_node in connection_array[node_]:
            if zero_one[candidate_node] == 0:
                improve_node_array.append(candidate_node)
    now_number *= -1
    for node_ in improve_node_array:
        zero_one[node_] = now_number

    now_node = improve_node_array

for _ in range(q):
    c, d = map(int, input().split())
    if zero_one[c - 1] == zero_one[d - 1]:
        print("Town")
    else:
        print("Road")
