def main():
    deck_list = list()
    input_file = open("R2.in", "r")
    output_file = open("r2.out", "w")
    t = int(input_file.readline())
    for i in range(t):
        pos_a = 0
        pos_z = 0
        pos_y = 0
        pos_b = 0
        for j in range(1000):
            deck = input_file.readline()
            for c in range(len(deck)):
                if deck[c] == 'A':
                    pos_a += c
                if deck[c] == 'z':
                    pos_z += c
                if deck[c] == 'B':
                    pos_b += c
                if deck[c] == 'y':
                    pos_y += c

        pos_a //= 1
        pos_z //= 1
        pos_b //= 1
        pos_y //= 1
        if abs(pos_a - pos_z) + abs(pos_y - pos_b) > 2500:
            output_file.write('riffle\n')
        else:
            output_file.write('uniform\n')
    input_file.close()
    output_file.close()


main()

