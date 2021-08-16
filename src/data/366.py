from collections import deque

n, q = map(int, input().split())
#print(n,q)

m = n - 1
#create adjacency list
g = [[] for _ in range(n + 1)]
#print(g)
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
#print(g)

#create depth_list
depth_list = [-1 for _ in range(n + 1)]
#print(depth_list)

#create rooted tree
dq = deque()
dq.append((1, 0))  #1. put first element(n,depth)
#print(len(q))
while len(dq) > 0:
    [a, d] = dq.pop()
    #print(a,d)
    depth_list[a] = d  # 2. confirm n's depth
    for child in g[a]:  #3. push child node
        if depth_list[child] >= 0:
            continue
        dq.append((child, d + 1))
#print(depth_list)

for i in range(q):
    a, b = map(int, input().split())
    if (depth_list[a] + depth_list[b]) % 2 == 0:
        print("Town")
    else:
        print("Road")
