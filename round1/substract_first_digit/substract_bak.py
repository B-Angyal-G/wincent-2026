import random

def get_length(n):
    l = 0
    while n != 0:
        n = n // 10
        l += 1
    return l - 1

def substarcting_old(n):
    l = get_length(n)
    s = 0
    while n != 0:
        first_digit = n // (10 ** l)
        if first_digit == 0:
            l -= 1
        else:
            n -= first_digit
            s += 1
    return s


def substarcting(n):
    l = get_length(n)
    s = 0
    while n != 0:
        first_digit = n // (10 ** l)
        if first_digit == 0:
            l -= 1
        else:
            rest = n - first_digit * 10 ** l
            part_sub = rest // first_digit + 1
            n = n - part_sub * first_digit
            s += part_sub
            # print('In func. n = ', n)
            # print('In func. F_dig = ', first_digit)
            # print('In func. rest = ', rest)
            # print()
    return s
    

def main():
    n = 4567890123
    l = get_length(n)
    first_digit = n // (10 ** l)
    rest = n - first_digit * 10 ** l
    part_sub = rest // first_digit + 1
    print(substarcting(n))
    print(substarcting_old(n))
    return 0

    print(n)
    print(l)
    print(first_digit)
    print(rest)
    print(part_sub)
    print(n - part_sub * first_digit)
    return 0
    # n = 29
    # if substarcting_old(n) - substarcting(n) != 0:
    #     print('HIBA: ', n)
    # print(substarcting(n))
    # return 0
    # for i in range(100):
    #     print("i = ", i)
    #     n = random.randint(1, 99999999)
    #     if substarcting_old(n) - substarcting(n) != 0:
    #         print(n)
    # return 0

    input_file = open("S2.in", "r")
    output_file = open("s2.out", "w")
    t = int(input_file.readline())
    for i in range(t):
        n = int(input_file.readline())
        output_file.write(str(substarcting(n)) + '\n')
    input_file.close()
    output_file.close()


main()
