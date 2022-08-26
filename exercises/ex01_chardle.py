"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730463283"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a signle character.")
    exit()
letter_instances: int = 0
print("Searching for " + single_character + " in " + word)
if single_character == word[0]:
    print(single_character + " found at index 0")
    letter_instances: int = letter_instances + 1
if single_character == word[1]:
    print(single_character + " found at index 1")  
    letter_instances: int = letter_instances + 1
if single_character == word[2]:
    print(single_character + " found at index 2")
    letter_instances: int = letter_instances + 1
if single_character == word[3]:
    print(single_character + " found at index 3")
    letter_instances: int = letter_instances + 1
if single_character == word[4]:
    print(single_character + " found at index 4")
    letter_instances: int = letter_instances + 1
if letter_instances == 0:
    print("No instances of " + single_character + " found in " + word)
if letter_instances == 1:
    print("1 instance of " + single_character + " found in " + word)
if letter_instances == 2:
    print("2 instances of " + single_character + " found in " + word)
if letter_instances == 3:
    print("3 instances of " + single_character + " found in " + word)
if letter_instances == 4:
    print("4 instances of " + single_character + " found in " + word)
if letter_instances == 5:
    print("5 instances of " + single_character + " found in " + word)
