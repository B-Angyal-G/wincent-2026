import itertools
import math

def combination(n, k, p):
    if k == 1:
        if p == 1:
            return [1, [0]]
        else:
            return [1]

    if n == k:
        if p == 1:
            return [1, list(range(n))]
        else:
            return [1]

    if k == 2:
        if n == 2:
            if p == 1:
                return [1, [0, 1]]
            else:
                return [1]
        elif n == 3:
            if p == 1:
                return [3, list(itertools.combinations([0, 1, 2], 2))]
            else:
                return [3]
        else:
            num_list = list([0] for i in range(n - 1))
            if p == 1:
                for i in range(len(num_list)):
                    num_list[i].append(i + 1)
                return [len(num_list), num_list]
            else:
                return [len(num_list)]
        

    result = combination_calc(n, k)
    if result[1] == 0:
        if p == 1:
            certains = list(itertools.combinations( list(range(1, n)), k - 1 ))
            num_list = list([0] for i in range(len(certains)))
            for i in range(len(certains)):
                num_list[i].extend(certains[i])

            return [len(certains), num_list]
        else:
            return [result[0]]
    elif result[1] == 1:
        if p == 1:
            all_comb = list(itertools.combinations( list(range(0, n)), k ))

            return [len(all_comb), all_comb]
        else:
            return [result[0]]


    # delete = list()
    # comb = list(itertools.combinations(list(range(n)), k))
    # for c in range(1,len(comb)):
    #     for past_c in range(c):
    #         if set(comb[c]).intersection(set(comb[past_c])) == set():
    #             delete.append(c)
    #             break
    # for i in range(len(delete) - 1, -1, -1):
    #     comb.pop(delete[i])

    # if p == 1:
    #     ret = [len(comb)]
    #     ret.extend(comb)
    #     return [len(comb), comb]
    # else:
    # return [len(comb)]
    


def combination_calc(n, k):
    certain = math.comb(n - 1, k - 1)
    S = 0
    i = 0
    while i < k and n - 2 - i >= k -2:
        S += math.comb(n - 2 - i, k -2)
        i += 1

    if S < certain:
        return [certain, 0]
    else:
        return [math.comb(n, k), 1]



def main():
    input_file = open("K5.in", "r")
    output_file = open("k5.out", "w")
    t = int(input_file.readline())
    for i in range(t):
        line = list(map(int, input_file.readline().strip().split(" ")))
        n = line[0]
        k = line[1]
        p = line[2]

        res = combination(n, k, p)
        if p == 0:
            output_file.write(str(res[0]) + '\n')
        else:
            output_file.write(str(res[0]) + '\n')
            for j in res[1]:
                if isinstance(j, (list, tuple)):
                    for e in j:
                        output_file.write(str(e) + " ")
                    output_file.write("\n")
                else:
                    output_file.write(str(j) + "\n")

    input_file.close()
    output_file.close()


main()

