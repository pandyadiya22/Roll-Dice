import random
def roll_dice():
    return random.randint(1,6)
def dice_reaction(number):
    reactions={
        1:"oof 1 again",
        2:"Not bad not good",
        3:"you are warming up",
        4:"Hey,luck is definately on your side",
        5:"You are fire!",
        6:"SIX! Jackpot yeyyy"
    }
    return reactions[number]
print("Welcome to the smart digital dice!")

while True:
    input("\nPress Enter to roll dice")
    number=roll_dice()
    print("you rolled:",number)
    print(dice_reaction(number))
    