#Basic guessing game

secret_word = "giraffe"
i = 1
guess = input("Guess the secret word: ")

while guess != secret_word and i < 3: 
       guess = input("You guessed wrong.Try again!:" )
       i += 1

if guess == secret_word:
    print("Congrats, You WIN! " + secret_word + " was right.")
else:
    print("You lose")
