from random import randint

class Die:
    def __init__(self):
        pass
        
    def dice():
        s = randint(1,6)
        if s == 1:
            print(" __________ ")
            print("|          |")
            print("|          |")
            print("|    ()    |")
            print("|          |")
            print("|__________|")
            print("    ONE     ")
        elif s == 2:
            print(" __________ ")
            print("|          |")
            print("|  ()      |")
            print("|          |")
            print("|      ()  |")
            print("|__________|")
            print("    TWO     ")
        elif s == 3:
            print(" __________ ")
            print("|          |")
            print("|  ()      |")
            print("|    ()    |")
            print("|      ()  |")
            print("|__________|")
            print("   THREE    ")
        elif s == 4:
            print(" __________ ")
            print("|          |")
            print("|  ()  ()  |")
            print("|          |")
            print("|  ()  ()  |")
            print("|__________|")
            print("    FOUR    ")
        elif s == 5:
            print(" __________ ")
            print("|          |")
            print("|  ()  ()  |")
            print("|    ()    |")
            print("|  ()  ()  |")
            print("|__________|")
            print("    FIVE    ")
        elif s == 6:
            print(" __________ ")
            print("|          |")
            print("|  ()  ()  |")
            print("|  ()  ()  |")
            print("|  ()  ()  |")
            print("|__________|")
            print("    SIX     ")


    dice()