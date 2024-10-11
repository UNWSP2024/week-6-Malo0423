import random
TOSSES = 100


def randDice():
    dice1 = random.randint (1, 6)
    dice2 = random.randint (1, 6)
    dice_sum = dice1 + dice2
    return dice_sum
def main():
    total = 0
    for toss in range (TOSSES):
        subtotal = randDice()
        total += subtotal
        average = total / 100
    print(f'The average is {average:,.2f}')

if __name__ == '__main__':
    main()



