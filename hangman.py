import random
words = ["apple", "house", "table", "river", "green"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    letter = input("Enter a letter: ").lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)
if "_" not in guessed:
    print("You Won! Word is", word)
else:
    print("You Lost! Word was", word)
