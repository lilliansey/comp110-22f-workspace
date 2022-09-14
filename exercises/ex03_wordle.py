"""EX03 - Structured Wordle."""

__author__ = "730463283"


# this function determines if there will be a yellow or white box
# searches the secret word for a letter in the guessed word at an index
def contains_char(searched: str, single_char: str) -> bool:
    """This function searches the secret word for a character."""
    assert len(single_char) == 1
    idx: int = 0
    while idx < len(searched):
        if searched[idx] == single_char:
            return True
        else:
            idx += 1
    return False 


# these represent the codes for the emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# this function assigns an emoji to the index of the word if guess is the same as, contains, or does not contain each letter
def emojified(guess: str, secret: str) -> str:
    """This function assigns emojis to each index of the guessed word."""
    assert len(guess) == len(secret)
    emoji_boxes: str = ""
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emoji_boxes = emoji_boxes + GREEN_BOX
        else:
            contains = contains_char(secret, guess[idx])
            if contains:
                emoji_boxes = emoji_boxes + YELLOW_BOX
            else:
                emoji_boxes = emoji_boxes + WHITE_BOX
        idx += 1
    return emoji_boxes


# this function will promp the user for a guess while making sure that the length of the guess matches the legth of the secret
def input_guess(expected_len: int) -> str:
    """Adding guess prompts."""
    choice: str = str(input(f"Enter a {expected_len} character word: "))
    while (len(choice)) != expected_len:
        choice = input(f"That wasn't {expected_len} chars! Try again: ")
    return choice


# the main function that starts the game and brings everything together
# also will keep track of turns and whether the game has been won or not
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = False
    answer: str = "codes"
    while won == (not True) and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = (input_guess(len(answer)))
        print(emojified(guess, answer))
        if guess == answer:
            print(f"You won in {turn}/6 turns!")
            won = True
        turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


# this makes it possible for other modules to import the code
if __name__ == "__main__":
    main()