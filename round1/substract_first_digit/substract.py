import sys

def get_length(n):
    l = 0
    while n != 0:
        n = n // 10
        l += 1
    return l - 1


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
            s = s % (10**9 + 7)
    return s
    

def main():
    sys.set_int_max_str_digits(0)
    input_file = open("S3.in", "r")
    output_file = open("s3.out", "w")
    t = int(input_file.readline())
    for i in range(t):
        print(i)
        n = int(input_file.readline())
        output_file.write(str(substarcting(n)) + '\n')
    input_file.close()
    output_file.close()


main()
