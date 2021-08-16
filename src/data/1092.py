N, Q = map(int, input().split())


def nibutan_ijyou(NUM, MAT):
    MIN = 0
    MAX = len(MAT) - 1
    while True:
        TMP = (MIN + MAX) // 2
        if MAT[TMP][0] < NUM:
            MIN = TMP
        elif MAT[TMP][0] >= NUM:
            MAX = TMP
        if MAX - MIN <= 1:
            break
    if MAT[MIN][0] >= NUM:
        MAX = MIN
    return MAX  #,MAT[MIN]


root_mat = []
for i in range(N - 1):
    A, B = map(int, input().split())
    root_mat.append([A, B])
    root_mat.append([B, A])

root_mat.sort()

#print(root_mat)

floor_mat = [0] * (N + 1)
check = [[1, 0]]
while True:
    if check == []:
        break
    now = check[-1][0]
    floor = check[-1][1]
    check.pop(-1)
    tmp = nibutan_ijyou(now, root_mat)
    while True:
        if root_mat[tmp][0] == now:
            next = root_mat[tmp][1]
            if floor_mat[next] == 0 and next != 1:
                check.append([next, floor + 1])
                floor_mat[next] = floor + 1
        else:
            break
        tmp += 1
        if tmp >= len(root_mat):
            break

#print(floor_mat)

for i in range(Q):
    T1, T2 = map(int, input().split())
    if (floor_mat[T1] + floor_mat[T2]) % 2 == 0:
        print("Town")
    else:
        print("Road")
