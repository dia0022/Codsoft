import random

options=("rock" , "paper" , "scissor")
running = True

while running:

    player= None
    computer= random.choice(options)

    while player not in options:
        player= input("Enter the choce(rock,paper, scissor):")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It is tie!!")

    elif player == "rock" and computer == "scissor":
        print("You win!!")

    elif player == "paper" and computer == "rock":
        print("you win!!")

    elif player == "scissor" and computer == "paper":
        print("you win!!")

    else:
        print("You lose!!")
    
    play = input("Play Again? (y/n):").lower()
    if not play == "y":
        running= False

print("Thanks for playing!")




