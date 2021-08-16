import sys

sys.setrecursionlimit(10**9)
N, Q = map(int, input().split())
#
next_town = [[] for _ in range(N)]
for k in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    next_town[a].append(b)
    next_town[b].append(a)

odd_or_even = [-1 for _ in range(N)]

town_lis = [0]
bit = 1
while town_lis:
    next_ = []
    for town in town_lis:
        odd_or_even[town] = bit
        for n_town in next_town[town]:
            if odd_or_even[n_town] == -1:
                next_.append(n_town)
    town_lis = next_
    bit ^= 1

#print(odd_or_even)
#
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if odd_or_even[c] == odd_or_even[d]:
        print('Town')
    else:
        print('Road')
