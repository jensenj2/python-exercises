while True:
    player1 = input("P1: Please enter 'rock', 'paper' or 'scissors': ")
    player2 = input("P2: Please enter 'rock' 'paper' or 'scissors': ")
    player1.lower()
    player2.lower()

    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins")
        elif player2 == "paper":
            print("Player 2 wins")
        else:
            print("No winners!")
    if player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins")
        elif player2 == "scissors":
            print("Player 2 wins")
        else:
            print("No winners!")
    if player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins")
        elif player2 == "rock":
            print("Player 2 wins")
        else:
            print("No winners!")
    replay = input("\nDo you wish to play again?")
    if replay == 'yes' or replay == 'y':
        print("RESTARTING...\n")
    elif replay == 'no' or replay == 'n':
        break