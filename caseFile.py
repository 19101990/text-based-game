import sys
import os
import time

t = 1

class Player():
    def __init__(self, name, surname, sex, age, position="StartRoom"):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.position = position


def prompt_for_name():
    os.system("cls")
    print("""Welcome to Hazardville Police Department. Please fill this form
with your personal data and experience to be considered for the
position of Hazardville sheriff.""")
    time.sleep(t)
    print("\n")
    global name_option
    name_option = input("NAME: ")
    prompt_for_surname()

def prompt_for_surname():
    global surname_option
    surname_option = input("SURNAME: ")
    prompt_for_sex()

def prompt_for_sex():
    global sex_option
    sex_option = input("SEX: ")
    if sex_option.lower() in ("m", "male", "man", "dude", "guy"):
        sex_option = "Mr."
    elif sex_option.lower() in ("f", "female", "woman", "girl", "chick"):
        sex_option = "Ms."
    prompt_for_age()

def prompt_for_age():
    global age_option
    age_option = input("AGE: ")
    global player
    player = Player(name_option, surname_option, sex_option, age_option)
    time.sleep(t)
    print("\n")
    print("We were really impressed with your resume {} {}.\n".format(player.sex.title(),
                                                                    player.surname.title()))
    print("""We decided we would like to offer you a position of Hazadrville's
Sheriff. Do you accept the offer?""")
    start()


def start():
    option = str(input("(Y/n): "))
    if option.lower() == "y":
        print("\n")
        print("Great! See you on Monday, Inspector!")
        take_action()
        os.system("cls")
        time.sleep(t)
        intro()
    elif option.lower() == "n":
        sys.exit()
    else:
        start()


def intro():
    print("2 years later...\n")
    take_action()
    os.system("cls")
    print("[SUNDAY, 1st of July, 07:21:30]\n")
    take_action()
    print("""You look through the window in you kitchen taking a sip of your
favourite tea. It's a lovely morning. And Hazardville is a lovely
town. Not even once during those two years you regretted your decision
about moving out from LA. Why would you? Nothing ever happened
here and you're a lazy """, end="")
    print("bastard" if player.sex == "Mr." else "bitch", end="")
    print(""" with absolutely no ambition to be a
good cop.""")
    take_action()
    print("""Suddenly you hear your phone ringing. \"Well, that's unusual\",
you think. You take just one more sip and answer the phone.""")
    time.sleep(t)
    print("\t- {}.".format(player.surname.title()))
    time.sleep(t)
    print("\t- Sir, " if player.sex == "Mr." else "\t- Ma'am,", " there's been a murder...\n")
    take_action()
    murder_scene()

def murder_scene():
    print("[Sunday, 1st of July, 7:40:45]\n")
    take_action()


def take_action():
    option_action = input("")
    if option_action == "":
        os.system("cls")
    elif option_action == "quit":
        sys.exit()
    else:
        take_action()

prompt_for_name()

# to be continued #
