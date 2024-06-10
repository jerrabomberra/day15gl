from random import randint

number =randint(1,100)
print(number)

def game(guesses):
    """Plays the game"""
    guess =int(input("Guess a number between 1 and 100. : "))
    while guess != number:
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"You guessed the number {number} correctly in {guesses} guesse(s). ")
    guesses +=1
    
guesses =0
play_game=True

while play_game == True:
    if guesses > 0:
        play_again = input("Do you want to play this game again? : ").lower()
    else:
        play_again = input("Do you want to play? : ").lower()
    if play_again == 'n':
        continue
    else:
        play_game = False
    guess = int(input("Guess again a number between 1 and 100. : "))
game(0)

