import random


def play():
    # let's the user choose rock, paper or scissors
    user_input = input("Rock, paper or scissors? (r, p, s): ")

    # Takes a random option between rock, paper or scissors and prints it out
    computer_input = random.choice(["r", "p", "s"])
    print("Computer chose: " + computer_input)

    # Compares the user and computer inputs and decided if it's a tie
    if user_input == computer_input:
        return "It's a tie"
    
    # Compares the user and computer inputs and decided if it's a win
    if win(user_input, computer_input):
        return "You won!"
    
    # If it's not a tie or a win, it must be a loss
    return "You lost!"


# Function that compares the user input and the computer input to see if you won
def win(player, opponent):
    if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

# starts the game
print(play())