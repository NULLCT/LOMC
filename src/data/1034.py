import sys


def getInt():
    return map(int, sys.stdin.readline().strip().split())


def getIntList():
    return list(map(int, sys.stdin.readline().strip().split()))


def getString():
    return sys.stdin.readline().strip()


def printOne(n):
    return sys.stdout.write(str(n) + "\n")


def printList(n):
    return sys.stdout.write("".join(map(str, n)) + "\n")


n, q = getInt()
g = [[] for _ in range(n + 1)]
#print(g)
for _ in range(n - 1):
    a, b = getInt()
    g[a].append(b)
    g[b].append(a)
now = [1]
rank = [0] * (n + 1)
check = [False] * (n + 1)
countx = 0
#print(g)
check[1] = True
while len(now) > 0:
    #print(now)
    #print("---------")
    new = []
    for x in now:
        rank[x] = countx
        for y in g[x]:
            if not check[y]:
                check[y] = True
                new.append(y)
    countx += 1
    now = new
#print(rank)
for _ in range(q):
    a, b = getInt()
    if abs(rank[a] - rank[b]) % 2 == 0: print("Town")
    else: print("Road")
