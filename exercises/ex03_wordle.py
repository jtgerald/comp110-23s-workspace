"""EX03 - Structured Wordle"""

__author__ = "730475086"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, i: str) -> bool:
    assert len(i) == 1
    if i in word: 
        return True
    else:
        return False
    
def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    emoji: str = ""
    c: int = 0
    total: int = len(guess) - 1
    while c <= total:
        if contains_char(secret, guess[c]) is True and guess[c] != secret[c]:
            emoji += YELLOW_BOX
        if contains_char(secret, guess[c]) is True and guess[c] == secret[c]:
            emoji += GREEN_BOX
        if contains_char(secret, guess[c]) is False:
            emoji += WHITE_BOX
        c += 1
    return emoji

def input_guess(number: int) -> str:
    user_input: str = input(f"Enter a {number} character word: ")
    while len(user_input) != number:
        if len(user_input) < number or len(user_input) > number:
            user_input = input(f"That wasn't {number} chars! Try again: ")
    return user_input

def main() -> None:
    secret: str = "codes"
    guess: str = " "
    count: int = 1
    while guess != secret:
        print(f"=== Turn {count}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if count <= 6 and guess != secret:
            count += 1
        if count >= 1 and guess == secret:
            print(f"You won in {count}/6 turns!")
            guess = secret
        if count == 7:
            print("X/6 - Sorry, try again tomorrow!")
            guess = secret

if __name__ == "__main__":
    main()