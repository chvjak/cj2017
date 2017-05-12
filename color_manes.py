# more numerous (A) should be less or equal to sum of other two (A <= B + C)
# in B + C - A number of B should be equal to C

f = open("color_manes.txt")

def input2():
         res = f.readline()
         return res
def get_stables(ponies):
    # ponies is sorted descending
    # ponies[0][0] <= ponies[1][0] <= ponies[2][0]
    (N1, N2, N3), (color1, color2, color3) = zip(*ponies)
    delta_N23 = N2 - N3  # excess N2 ponies, N2 < N1 since N1 is max(N1, N2, N3

    if N1 > N2 + N3:
        return "IMPOSSIBLE"
    elif delta_N23 > N1:
        return "IMPOSSIBLE"
    else:
        res = [None] * (N1 + N2 + N3)

        ponies23 = [color2] * delta_N23

        fill_N23 = (N1 - delta_N23)          # the fill made of equal qulities of N2 and N3 to match the rest of N1

        ponies23 += [color2] * (fill_N23 // 2)  # MIND odd quantities! also odd N1!
        ponies23 += [color3] * (fill_N23 // 2)  # MIND odd quantities! also odd N1!

        if fill_N23 % 2 == 1:
            ponies23 += [color3]

        for i in range(N1):
            res[2 * i] = color1
            res[2 * i + 1] = ponies23[i]

        for i in range(2 * N1, N1 + N2 + N3):
            if i % 2 == 0:
                res[i] = color2
            else:
                res[i] = color3

        return res

T = int(input().strip())

for t in range(T):
    ponies_raw = [int(x) for x in input().strip().split(' ')]
    ponies = [(ponies_raw[ix], c) for ix, c in zip([1, 3, 5], ['R', 'Y', 'B'])]
    ponies.sort(reverse = True, key = lambda x: x[0])

    res = get_stables(ponies)

    print("Case #{}: {}".format(t + 1, ''.join(res)))
