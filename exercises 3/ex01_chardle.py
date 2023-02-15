"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730475086"

word_choice: str = input("Enter a 5-character word: ")
if len(word_choice) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word_choice)
n: int = 0
if (character == word_choice[0]):
    print(str(character) + " found at index 0")
    n = n + 1

if (character == word_choice[1]):
    print(str(character) + " found at index 1")
    n = n + 1

if (character == word_choice[2]):
    print(str(character) + " found at index 2")
    n = n + 1

if (character == word_choice[3]):
    print(str(character) + " found at index 3")
    n = n + 1

if (character == word_choice[4]):
    print(str(character) + " found at index 4")
    n = n + 1

if n == 1:
    print(str(1) + " instance of " + str(character) + " found in " + word_choice)

if n > 1:
    print(str(n) + " instances of " + str(character) + " found in " + word_choice)

if n == 0:
    print("No instances of " + str(character) + " found in " + word_choice)