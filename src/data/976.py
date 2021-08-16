import sys, collections, math, itertools, re, decimal, statistics

sys.setrecursionlimit(200000)
# n = int(input())
n, q = map(int, input().split())
# li = list(map(int,input().split()))
li = []
for i in range(n - 1):
    li.append(list(map(int, input().split())))
hash = {}
for i in range(n - 1):
    if li[i][0] not in hash: hash[li[i][0]] = [li[i][1]]
    else: hash[li[i][0]].append(li[i][1])
    if li[i][1] not in hash: hash[li[i][1]] = [li[i][0]]
    else: hash[li[i][1]].append(li[i][0])
#print(hash)

# def rec(x,cnt):
#     for y in hash[x]:
#         if seen[y] == -1:
#             seen[y] = cnt
#             rec(y,0 if cnt else 1)
#     return

# rec(1,1)

#print(seen)
cd = []
for i in range(q):
    cd.append(list(map(int, input().split())))

seen = [-1] * (n + 1)

d = [[1, 1]]
while d:
    x = d.pop()
    seen[x[0]] = x[1]
    for y in hash[x[0]]:
        if seen[y] == -1:
            d.append([y, 0 if x[1] else 1])

for c, d in cd:
    print("Town" if seen[c] == seen[d] else "Road")
