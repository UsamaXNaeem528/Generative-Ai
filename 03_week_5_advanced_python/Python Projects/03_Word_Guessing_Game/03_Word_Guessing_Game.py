import random

#secret lists
easy_words = ["apple", "book", "chair", "water", "happy"]

medium_words = ["journey", "village", "library", "beautiful", "mountain"]

difficult_words = ["benevolent", "meticulous", "exuberant", "phenomenon", "eloquent"]

#welcome message
print("Welcome to word guessing game")
print("Choose the difficculy level of Words Easy, Medium, Difficult words for game")

#getting difficulty level from user
level = input("Kindly enter the level difficulty : ").lower()
secret = ''

if level == 'easy':
    secret = random.choice(easy_words)
elif level == 'medium':
    secret = random.choice(medium_words)
elif level == 'difficult':
    secret = random.choice(difficult_words)
else:
    print("Kindly Enter Correct difficulty Level")

print(f"Secret words contains a {len(secret)} letters")
print(f"Secret Word ", secret)

attempts = 0

while True:
    guess = input("Enter the guess word : ").lower()
    attempts += 1
    hint = ''
    if secret == guess:
        print(f"Congratulation You Correctly Guess the secret word in {attempts} Attempt")
        break
    else:
        if len(guess) >= len(secret):   # if user enters same or more characters than secret
            is_match = True
            for i in range(len(secret)):  # this loop check the if any match word in guesss as compared to secret then break the loop isMAtch become false
                if guess[i] != secret[i]:
                    is_match = False
                    break

            if is_match:
                if len(guess) > len(secret):
                    print("Almost correct! You added extra letters at the end.")
                print(f"Congratulations! You guessed the secret word in {attempts} attempts.")
                break
            else:
                # Partial match but same/longer guess OR if no match
                hint = ""
                for i in range(len(secret)):
                    if i < len(guess) and secret[i] == guess[i]:
                        hint += secret[i]
                    else:
                        hint += "_"
                print("Hint:", hint)

        else:
            # When guess is shorter than the secret
            hint = ""
            for i in range(len(secret)):
                if i < len(guess) and secret[i] == guess[i]:
                    hint += secret[i]
                else:
                    hint += "_"
            print("Hint:", hint)
