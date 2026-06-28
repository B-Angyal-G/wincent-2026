def get_n_k(line):
    n = ""
    k = ""
    i = 0
    while line[i] != " ":
        i += 1
    n = line[0:i]
    k = line[i + 1:len(line) - 1]
    return [int(n), int(k)]

def get_heights(line):
    heights = list()
    h = ""
    for i in range(len(line)):
        if line[i] == " " or line[i] == "\n":
            heights.append(int(h))
            h = ""
        else:
            h += line[i]
    return heights

        
def cut_circle(indexes, max_ind, min_ind):
    if max_ind < min_ind:
        max_ind, min_ind = min_ind, max_ind

    for i in range(len(indexes)):
        if indexes[i] == min_ind:
            min_i = i
        if indexes[i] == max_ind:
            max_i = i
    
    l1 = indexes[0 : min_i]
    l2 = indexes[min_i + 1 : max_i]
    l3 = indexes[max_i + 1 : len(indexes)]
    l1.extend(l3)

    return [ l1, l2 ]


def construct_slides(heights, n, k):
    # if k == 1:
    #     return [heights.index(max(heights)), heights.index(min(heights))]
    # else:
    #     return [-1, -1]
    res = list()

    indexes = list(range(n))
    index_sets = [indexes]
    sorted_heights = sorted(heights, reverse=True)
        

    i_max = 0
    i_min = len(heights) - 1
    i_max_limit = i_max
    i_min_limit = i_min
    
    END = 0
    CHOOSEN = 0
    while (True):
        max_ind = heights.index(sorted_heights[i_max])
        min_ind = heights.index(sorted_heights[i_min])
        for set_ind in range(len(index_sets)):
            # Kiválasztás
            if max_ind in index_sets[set_ind] and min_ind in index_sets[set_ind]:
                res.append([max_ind, min_ind])
                tmp_sets = cut_circle(index_sets[set_ind], max_ind, min_ind)
                index_sets.pop(set_ind)
                index_sets.extend(tmp_sets)
                k -= 1
                if k == 0:
                    END = 1
                    break
                CHOOSEN = 1
        if END == 1:
            return res

        if CHOOSEN == 1:
            i_max -= 1
            i_min += 1
            i_max_limit = i_max
            i_min_limit = i_min
            CHOOSEN = 0
        else:
            i_min += 1

            if max_ind == min_ind:
                i_max -= 1
                i_min = i_min_limit

                if i_max == i_min:
                    # VISSZALÉPÉS
                    last_res = res.pop(-1)




            

def main():
    ma = 3
    mi = 6
    ind = list(range(12))
    print(ind)
    print(cut_circle(ind, ma, mi))
    return 0

    # indexes = [4, 5, 6, 7, 8, 9, 10, 11]
    # max_ind = 6
    # min_ind = 9
    # for i_min in range(len(indexes) - 1, 0, -1):
    #     print(indexes[i_min])
    # return 0

    input_file = open("W1.in", "r")
    output_file = open("w1.out", "w")
    t = int(input_file.readline())
    for i in range(1):
        nk = get_n_k(input_file.readline())
        heights = get_heights(input_file.readline())

        print(heights)
        res = construct_slides(heights, nk[0], nk[1])
        print()
        # output_file.write(str(res[0]) + " " + str(res[1]) + '\n')
    input_file.close()
    output_file.close()


main()

