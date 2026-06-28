def get_length(n):
    l = 0
    while n != 0:
        n = n // 10
        l += 1
    return l

def first_digit(n):
    return n // 10**(get_length(n) - 1)

def without_first_digit(n):
    return n - (first_digit(n) * 10 ** (get_length(n) - 1))


def substracting(n):
    s = 0
    i = 0
    PRINT = 0
    while n != 0:
        if i < 20:
            PRINT = 1
        else:
            PRINT = 0
        if PRINT == 1:
            print('n: ', n)
        f_digit = first_digit(n)
        rest = without_first_digit(n)
        s_part = rest // f_digit + 1
        n = n - s_part * f_digit
        s += s_part
        if PRINT == 1:
            print('f: ', f_digit)
            print('r: ', rest)
            print('p: ', s_part)
            print('n: ', n)
            print('s: ', s)
            print()
        i += 1
    return s


def main():
    n = 4567890123
    print(n)
    print(get_length(n))
    print(first_digit(n))
    print(without_first_digit(n))
    print('res: ', substracting(n) % (10**9 + 7))
    return 0
    input_file = open("S0_sample2.in", "r")
    output_file = open("s02.out", "w")
    t = int(input_file.readline())
    for i in range(t):
        n = int(input_file.readline())
        output_file.write(str(substracting(n)) + '\n')
    input_file.close()
    output_file.close()


main()
