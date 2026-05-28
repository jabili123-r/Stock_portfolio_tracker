word = "apple"

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 You guessed the word correctly!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Enter only one letter!")

    elif guess in guessed_letters:
        print("You already guessed this letter!")

    elif guess in word:
        print("Correct!")
        guessed_letters.append(guess)

    else:
        print("Wrong guess!")
        wrong_guesses += 1
        guessed_letters.append(guess)
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\nYou lost!")
    print("The word was:", word)