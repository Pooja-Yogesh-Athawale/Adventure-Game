# import modules :
import time
import random


# list of Weapons:
weapons = random.choice(["Shield", "Repulsor", "Hammer", "Axe"])


# Print_pause :
def print_pause(message):
    print(message)
    time.sleep(1)


# Main Intro:
def intro():
    print_pause(" Suppose you are the Avenger Hero! ")
    print_pause(" You are supposed to save the Earth ")


# Accepting the Challenge :
def accept_challenge():
    response = input(" Want to accept the Challenge ? yes or no ").lower()
    if response == "yes":
        print_pause(" Great! Get ready!!!!!! ")
        fight(weapons)
    elif response == "no":
        print_pause(" You should accept the Challenge ")
        new_game()
    else:
        print_pause(" Please type Correct Option ")
        accept_challenge()


# Fight:
def fight(weapons):
    print_pause(" For increasing your power , You Got " + weapons + " ! ")
    print_pause(" To help you to win your Challenge ")
    response = input(" Whom did you choose : thor or hulk ? ").lower()
    if response == "thor":
        print_pause(" Yay ! You Chose " + weapons + " Thor 's Hammer ")
        print_pause(" Get ready to fight ")
        thor(weapons)
    elif response == "hulk":
        print_pause(" So You chose " + weapons + " Hulk's Axe ")
        print_pause(" Get ready to fight ")
        hulk(weapons)
    else:
        print(" Invalid Input ")
        fight(weapons)


# Thor:
def thor(weapons):
    print_pause(" Ugly giant Toad Started fighting with you ")
    print_pause(" Hurray! You won the Challenge ")
    new_game()


# hulk:
def hulk(weapons):
    print_pause(" Weired danger Creature Started fighting with you ")
    print_pause(" Hurray! You won the Challenge ")
    new_game()


# New Game:
def new_game():
    response = input(" Do you want to play again   ?  yes or no ").lower()
    if response == "yes":
        print_pause(" Okay! Let's Start ")
        play_game()
    elif response == "no":
        print_pause(" Thank You Byee!!!! ")
        exit(0)
    else:
        print_pause(" Please type yes or no ! ")


# Play Game:
def play_game():
    intro()
    accept_challenge()
    fight(weapons)
    thor(weapons)
    hulk(weapons)
    new_game()
play_game()