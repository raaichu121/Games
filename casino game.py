import random

def casino_game():
    print("Welcome to the Casino Game!")
    print("You have 100 chips to start with. Let's play!\n")
    
    chips = 100
    while chips > 0:
        print("You have {} chips".format(chips))
        bet = int(input("How many chips would you like to bet? "))
        
        while bet > chips:
            print("You don't have enough chips to make that bet. Please enter a valid amount.")
            bet = int(input("How many chips would you like to bet? "))
        
        roll = random.randint(1, 6)
        print("You rolled a {}".format(roll))
        
        if roll in [1, 2, 3]:
            chips -= bet
            print("You lost {} chips.\n".format(bet))
        elif roll in [4, 5, 6]:
            chips += bet
            print("You won {} chips!\n".format(bet))
    
    print("You have no chips left. Thank you for playing the Casino Game!")

casino_game()
