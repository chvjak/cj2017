#f = open("B-small-attempt1.in")
#f = open("tidy1.txt")

#def input():
#     res = f.readline()
#     return res

T = int(input().strip())
for t in range(T):
    N = input().strip()


    prev_c = N[0]
    res = prev_c
    for ci in range(1, len(N)):
        c = N[ci]
        if int(prev_c) > int(c):    # 1210 => 1199
            ci -= 1
            while ci > -1 and int(N[ci]) == 1:
                ci -= 1

            while ci > 0 and int(N[ci]) == int(N[ci - 1]):  # 998 => 899; 9998 => 8999; 122210 => 119999; 221 => 199
                ci -= 1

            if ci > -1:
                res = res[:ci] + str(int(N[ci]) - 1)
                res += "9" * (len(N) - ci - 1)
            else:
                res = "9" * (len(N) - ci - 2)
            break

        else:
            res += c
            prev_c = c

    print("Case #{}: {}".format(t + 1, res))





