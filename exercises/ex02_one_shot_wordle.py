"""One Shot Wordle!"""

_author_ = "730475086"

secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
ind: int = 0
store: str = ""

wordle: str = input(f"What is your {len(secret)} letter guess? ")

while len(wordle) != len(secret):
    wordle = input(f"That was not {len(secret)} letters! Try again: ")

while ind < len(secret):
    if wordle[ind] == secret[ind]:
        store = store + GREEN_BOX
    else:
        existing: bool = False
        exist_anywhere: int = 0
        while exist_anywhere < len(secret):
            if (secret[exist_anywhere]) == (wordle[ind]):
                store = store + YELLOW_BOX
                existing = True
                exist_anywhere = len(wordle)
            else:
                exist_anywhere = exist_anywhere + 1
        if not existing:
            store = store + WHITE_BOX
    ind = ind + 1
        
print(store)

if secret == wordle:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")