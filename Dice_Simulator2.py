import random
def win_lose(a,b):
    if a==b:
        print("You Win!!!!!")
    else:
        print("You Lose!!!!!")
choice="y"
while (choice=="y"):
    choice = input(str("enter y for rolling dice or n for stop"))
    if choice=="y":
        x=random.randint(1,6)
        k=random.randint(1,6)
        print("Dice 1:",x)
        print("Dice 2:",k)
        win_lose(x,k)
    else:
        break