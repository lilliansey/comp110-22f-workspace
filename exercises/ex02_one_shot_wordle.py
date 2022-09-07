"""EX02 - One Shot Wordle."""

__author__ = "730463283"

secret_word: str = "python"
guess = str = input(f"What is your {len(secret_word)}-letter guess? ")
index_guess: int = 0
emoji_boxes = ""
WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8" 
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
while index_guess < len(secret_word):
    if secret_word[index_guess] == guess[index_guess]:
        emoji_boxes = emoji_boxes + GREEN_BOX
    else:
        inside_guess: bool = False
        alt_index: int = 0
        while inside_guess is not True and alt_index < len(secret_word):
            if secret_word[alt_index] == guess[index_guess]:
                inside_guess = True
            else:
                alt_index += 1
        if inside_guess is True:
            emoji_boxes = emoji_boxes + YELLOW_BOX
        else:
            emoji_boxes = emoji_boxes + WHITE_BOX
    index_guess += 1
print(emoji_boxes)
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")