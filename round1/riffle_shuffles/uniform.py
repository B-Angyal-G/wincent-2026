import random

def uniform_shuffle():
    deck = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    shuff_deck = ''
    for _ in range(52):
        index = random.randint(0, len(deck) - 1)
        shuff_deck += deck[index]
        deck = deck[:index] + deck[index + 1:]
    return shuff_deck

def main():
    output_file = open("own_uniform_shuffle.in", "w")
    for _ in range(1000):
        output_file.write(uniform_shuffle() + '\n')
    output_file.close()

main()
