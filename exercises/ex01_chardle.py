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
