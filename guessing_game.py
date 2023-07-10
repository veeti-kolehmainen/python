secret_word = "giraffe"
guess = ""
guess_lives = 3
guess_limit = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_lives > guess_limit:
        guess = input("Enter guess: ")
        guess_lives -= 1
    else:
        out_of_guesses = True
    if guess != secret_word and not(out_of_guesses):
        print("(" + str(guess_lives) + " lives left)")

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")
