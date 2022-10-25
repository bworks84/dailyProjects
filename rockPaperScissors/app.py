import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit game: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("game ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("There is a tie, go again!")
        elif computer_input == "paper":
            computer_points += 1
            print("Your input is rock, computer input is paper. Computer wins...")
        elif computer_input == "scissors":
            user_points += 1
            print("Your input is rock, computer input is scissor. User wins...")
