f = open("alphabet_cake.txt")
#f = open("A-small-practice.in")
#
def input2():
         res = f.readline()
         return res

def get_res_cake(cake):
    def all_distributed():
        for row in res_cake:
            if '?' in row:
                return False
        else:
            return True

    def is_valid_expansion(expansion, c):
        min_i, min_j, max_i, max_j = expansion
        for i in range(min_i, max_i + 1):
            for j in range(min_j, max_j + 1):
                if res_cake[i][j] not in ('?', c):
                    return False
        else:
            return True

    def do_expansion(expansion, c):
        min_i, min_j, max_i, max_j = expansion
        for i in range(min_i, max_i + 1):
            for j in range(min_j, max_j + 1):
                res_cake[i][j] = c

    def undo_expansion(expansion):
        do_expansion(expansion, '?')

    def is_valid(r, c):
        R = len(res_cake)
        C = len(res_cake[0])
        return r < R and c < C and r >= 0 and c >= 0

    def get_expansions(pos):
        i,j = pos

        i += 1
        while is_valid(i, j) and res_cake[i][j] == '?':
            i += 1
        max_i = i - 1

        i, j = pos
        i -= 1
        while is_valid(i, j) and res_cake[i][j] == '?':
            i -= 1
        min_i = i + 1

        i, j = pos
        j += 1
        while is_valid(i, j) and res_cake[i][j] == '?':
            j += 1
        max_j = j - 1

        i, j = pos
        j -= 1
        while is_valid(i, j) and res_cake[i][j] == '?':
            j -= 1
        min_j = j + 1

        expansions = []

        i0, j0 = pos
        for i1 in range(min_i, i0 + 1):
            for j1 in range(min_j, j0 + 1):
                for i2 in range(i0, max_i + 1):
                    for j2 in range(j0, max_j + 1):
                        expansions.append((i1, j1, i2, j2))
        return expansions

    def add_initials(ii):
        rc = res_cake
        if all_distributed():
            return True

        if ii == len(initials):
            return False

        ch = initials[ii]
        expansions = get_expansions(initial_pos[ch])
        for expansion in expansions:
            if is_valid_expansion(expansion, ch):
                do_expansion(expansion, ch)
                if add_initials(ii + 1):
                    return True
                else:
                    undo_expansion(expansion)
                    r,c = initial_pos[ch]
                    res_cake[r][c] = ch

        #none of the ways to expand did it
        return False

    res_cake = [None] * R
    initial_pos = {}
    for ri in range(R):
        row = cake[ri]
        res_cake[ri] = row[:]
        for ci in range(C):
            c = row[ci]
            if c != '?':
                initial_pos[c] = (ri, ci)

    initials = list(initial_pos.keys())
    #print(initials)
    initials.sort()
    add_initials(0)

    return res_cake


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





