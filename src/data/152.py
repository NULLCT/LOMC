N, Q = list(map(int, input().split()))

a = list()
b = list()
c = list()
d = list()
connection = list()
for i in range(N + 1):
    connection.append([])

for i in range(N - 1):
    a_, b_ = list(map(int, input().split()))
    a.append(a_)
    b.append(b_)
    connection[a_].append(b_)
    connection[b_].append(a_)

for i in range(Q):
    c_, d_ = list(map(int, input().split()))
    c.append(c_)
    d.append(d_)

R = R = [100001] * (N + 1)


def distance():
    r = 0
    next_town = [1]
    next_town_memo = []

    while r < N:
        next_town_memo = []
        for town in next_town:
            if R[town] > r:
                R[town] = r
                for i in connection[town]:
                    next_town_memo.append(i)
        next_town = next_town_memo
        r = r + 1

    return R


distance()

for i in range(Q):
    e = R[c[i]] - R[d[i]]
    if e % 2 == 0:
        print('Town')
    else:
        print('Road')
