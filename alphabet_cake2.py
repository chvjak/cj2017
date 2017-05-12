#f = open("alphabet_cake.txt")
f = open("A-small-practice.in")
#
def input():
         res = f.readline()
         return res

def get_res_cake(cake):
    for row in cake:
        last_i = '?'
        for ci, c in enumerate(row):
            if c == '?':
                row[ci] = last_i
            else:
                if last_i == '?':
                    row[:ci] = [c] * ci
                last_i = c

    for ri in range(1, R):
        row = cake[ri]
        if row[0] == '?':
            cake[ri] = cake[ri - 1][:]

    for ri in reversed(range(0, R - 1)):
        row = cake[ri]
        if row[0] == '?':
            cake[ri] = cake[ri + 1][:]

    return cake

T = int(input().strip())

for t in range(T):
    R, C = [int(x) for x in input().strip().split(' ')]
    cake = [None] * R
    for ri in range(R):
        cake[ri] = list(input().strip())

    res_cake = get_res_cake(cake)

    print("Case #{}:".format(t + 1))
    for row in res_cake:
        print(''.join(row))





