#   HANGMAN
import random
from hangman_logo import logo
from hangman_words import word_list

print(logo)
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

correct_letter = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letter:
        print(f"You've already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You have only {lives} lives to live.")
        if lives == 0:
            game_over = True
            print("You lost! Game Over.")

    if "_" not in display:
        game_over = True
        print("You win")
