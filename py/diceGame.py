def dice():
    total = 1000
    import random
    game = "Y"
    while (game == "Y"):
        bbet = raw_input()
        bet = int(bbet)
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print "Roll is ", die1, " and ", die2
        if ((die1+die2)%2==0):
            print "You lose"
            total-=bet
        else:
            print "You win"
            total+=bet*2
        game = raw_input("Play again? (Y/N)")
    print "Final amount = ", total 