import random
from word_list_file import word_list
from hangman_art import logo, stages

# Variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# 'Hangman' logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # check if user has already guessed the same letter before
    if guess in display:
        print(f"You have already guessed {guess}, try another.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe word was '{chosen_word}'")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])