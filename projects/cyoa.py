"""EX06 - Choose Your Own Adventure."""

__author__ = "730463283"

# This program will simulate a buzzfeed quiz where you can find out your Harry Potter House.
from random import randint
player: str = "player name"
# main function starts here
points: int = 0
YELLOW_HEART = "\U0001F49B"
BOOK_EMOJI = "\U0001F4D8"
SNAKE_EMOJI = "\U0001F40D"
LION_EMOJI = "\U0001F981"

def main() -> None:
    """This is the main function."""
    print(greet())
    bounds: bool = True
    game_idx: int = 0
    while bounds is True:
        game: int = input(f"{player} would you like to find out your 1. patronus charm, 2. Hogwarts house, or 3. wandcore? ")
        game_idx = int(game)
        if game_idx > 0:
            if game_idx < 4:
                bounds = False
        else:
            bounds = True
            print(f"{player} please enter a 1, 2, or 3 if you would like to be sorted.")
    if game_idx == 1:
        print(charm())
    if game_idx == 2:
        print(house())
    if game_idx == 3:
        print(wandcore())
    

def greet() -> None:
    """This function greets the player and introduces them to the game."""
    print("Hello and welcome to the Sorting Ceremony!")
    print("Tonight you will be able to discover your patronus charm, hogwarts house, or wand core.")
    global player
    player = input("What is your name? ")
    print(f"Welcome to the sorting ceremony {player}!")



def charm() -> str:
    """This function will determine the players patronus charm."""
    bounds: bool = True
    object_idx: int = 0
    global points
    while bounds is True:
        object: int = input("Pick a magical object. 1. Firebolt, 2. Invisibility Cloak, 3. Time Turner, 4. Sneakoscope. ")
        print(f"You selected number {object}!")
        object_idx = int(object)
        if object_idx > 0:
            if object_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points =+ object_idx
    bounds = True
    drink_idx: int = 0
    while bounds is True:
        drink: int = input("Pick a magical drink. 1. Firewhisky, 2. Butterbeer, 3. Wolfsbane Tea, 4. Pumpkin Juice. ")
        print(f"You selected number {drink}!")
        drink_idx = int(drink)
        if drink_idx > 0:
            if drink_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points += drink_idx
    bounds = True
    shop_idx: int = 0
    while bounds is True:
        shop: int = input("Pick a magic shop 1. Zonkos, 2. Wesley's Wizarding Weezes, 3. Flourish and Blotts, 4. Borgin and Burkes. ")
        print(f"You selected number {shop}!")
        shop_idx = int(shop)
        if shop_idx > 0:
            if shop_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points += shop_idx
    if points >= 0:
        if points <= 4:
            return print("Your patronus is a black dog.")
        if points <= 7:
            return print("Your patronus is a stag")
        if points <= 10:
            return print("Your patronus is a wolf")
        if points <= 12:
            return print("Your patronus is a rat.")


def house() -> str:
    """This function will determine the players hogwarts House."""
    bounds: bool = True
    cheat_idx: int = 0
    global points
    while bounds is True:
        print("During your NEWT examinations you see one of your classmates using an illegal enchanted quill to get all the correct answers on their exam. ")
        cheat: int = input("Do you 1. Tell the professor immediatly because cheating is not allowed, 2. Nothing, but if they had done better than me I would tell the professor, 3. Give them a high five for being able to trick the exam, or 4. Encourage them to tell the professor themselves. ")
        print(f"You selected number {cheat}!")
        cheat_idx = int(cheat)
        if cheat_idx > 0:
            if cheat_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points =+ cheat_idx
    bounds = True
    feelings_idx: int = 0
    while bounds is True:
        print("Your feelings would be most hurt if someone called you a: ")
        feelings: int = input("1. Unkind, 2. Dumb, 3. Lazy, or 4. Weak? ")
        print(f"You selected number {feelings}!")
        feelings_idx = int(feelings)
        if feelings_idx > 0:
            if feelings_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points += feelings_idx
    bounds = True
    spell_idx: int = 0
    while bounds is True:
        print("On your way to the astronomy tower you are hit from behind with a jelly leg jinx, do you:")
        spell: int = input("1. Brush it off and walk away, they probably had a bad day. 2. Cast the counter spell and hurry so you don't miss class. 3. Don't let anyone else see you stumble and remember who they are for payback later. or 4. Curse them right back with a bat bogey hex.")
        print(f"You selected number {spell}!")
        spell_idx = int(spell)
        if spell_idx > 0:
            if spell_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points += spell_idx
    if points >= 0:
        if points <= 4:
            return print(f"You have been sorted into Hufflepuff {YELLOW_HEART}!!")
        if points <= 7:
            return print(f"You have been sorted into Ravenclaw {BOOK_EMOJI}!!")
        if points <= 10:
            return print(f"You have been sorted into Slytherin {SNAKE_EMOJI}!!")
        if points <= 12:
            return print(f"You have been sorted into Gryfindoor {LION_EMOJI}!!")


def wandcore() -> str:
    """This function will ask questions to determine what the players wand core is."""
    bounds: bool = True
    outgoing_idx: int = 0
    global points
    while bounds is True:
        print("How outgoing are you?")
        outgoing: int = input("1. Very outgoing, 2. Somewhat outgoing, 3. Not at all outgoing. ")
        print(f"You selected number {outgoing}!")
        outgoing_idx = int(outgoing)
        if outgoing_idx > 0:
            if outgoing_idx < 5:
                bounds = False
        else:
            bounds = True
            print("Please pick a number between 1 and 4.")
    points =+ outgoing_idx
    bounds = True
    char_idx: int = 0
    while bounds is True:
        print("Who is your favorite Harry Potter character")
        char: int = input("1. Harry Potter, 2. Draco Malfoy, 3. Luna Lovegood. ")
        print(f"You selected number {char}!")
        char_idx = int(char)
        if char_idx > 0:
            if char_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points += char_idx
    bounds = True
    power_idx: int = 0
    while bounds is True:
        print("What is your super power.")
        power: int = input("1. Flight, 2. Telekinesis, 3. Invisibility. ")
        print(f"You selected number {power}!")
        power_idx = int(power)
        if power_idx > 0:
            if power_idx < 5:
                bounds = False
        else:
            bounds = True
            print("please pick a number between 1 and 4.")
    points += power_idx
    first_spell: int = randint(0, 3)
    if first_spell == 0:
        print(f"{player} the first spell with your new wand will be lumos, which will light the tip of your wand.")
    if first_spell == 1:
        print(f"{player} the first spell with your new wand will be confundus, which will confuse the person it is casted at.")
    if first_spell == 2:
        print(f"{player} the first spell with your new wand will be aguamenti, which will make clean water spout from your wand.")
    if first_spell == 3:
        print(f"{player} the first spell with your new wand will be tarantallegra, which is the dancing feet spell.")
    if points >= 0:
        if points <= 4:
            return print("The core of your wand is Dragon Heart String.")
        if points <= 7:
            return print("The core of your wand is Phoenix Feather.")
        if points <= 9:
            return print("The core of your wand is Unicorn Horn")



if __name__ =="__main__":
    main()