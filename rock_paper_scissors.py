import random

def play():
    user_input = input("Rock, paper or scissors? (r, p, s): ")
    computer_input = random.choice(["r", "p", "s"])
    print("Computer chose: " + computer_input)

    if user_input == computer_input:
        return "It's a tie"
    
    if win(user_input, computer_input):
        return "You won!"
    
    return "You lost!"

def win(player, opponent):
    if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    
print(play())