import random

def riffle_shuffle(deck):
    n = len(deck)
    if n <= 1: return deck
    x = sum(1 for _ in range(n) if random.random() < 0.5)
    A, B = deck[:x], deck[x:]
    output = []
    aidx, bidx = 0, 0
    while aidx < len(A) and bidx < len(B):
        a, b = len(A)-aidx, len(B)-bidx
        if random.random() < a / (a+b):
            output.append(A[aidx])
            aidx += 1
        else:
            output.append(B[bidx])
            bidx += 1
    output += A[aidx:]
    output += B[bidx:]
    return output


def main():
    deck_orig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output_file = open("own_riffle_shuffle.in", "w")
    for _ in range(1000):
        deck = deck_orig
        for _ in range(7):
            deck = riffle_shuffle(deck)
        s = ''
        for i in deck:
            s += i
        output_file.write(s + '\n')
    output_file.close()

main()
