import random

def casino_game():
    print("-----------------------------")
    print(" Welcome to the Casino Game!")
    print("-----------------------------")
    name = input("Player name?\n")
    print("Hello " + name + "!")
    rup = int(input("\nHow much chips you want exchange. "))
    print("You have {} chips to start with. Let's play!\n".format(rup))
    
    Rupee = rup
    while Rupee > 0:
        print("You have {} chips".format(Rupee))
        bet = int(input("How many chips would you like to bet? "))
        
        while bet > Rupee:
            print("You don't have enough chips to make that bet. Please enter a valid amount.")
            bet = int(input("How many chips would you like to bet? "))
        
        print("Guess the face 1.diamond, 2.heart, 3.spade, 4.club, 5.flag & 6.Burja: ")
        guess = int(input())
        
        roll = random.randint(1, 6)
        print("The face was no. {}".format(roll))
        
        if guess == roll:
            Rupee += bet * 5
            print("You won {} chips!\n".format(bet * 5))
        else:
            Rupee -= bet
            print("You lost {} chips.\n".format(bet))
    
    print("You have no chips left. Thank you for playing the Casino Game!")

casino_game()