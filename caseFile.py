import sys
import os
import time

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
    time.sleep(1)
    print("\n")
    name_option = input("NAME: ")
    surname_option = input("SURNAME: ")
    sex_option = input("SEX: ")
    if sex_option.lower() in ("m", "male", "man", "dude", "guy"):
        sex_option = "Mr."
    elif sex_option.lower() in ("f", "female", "woman", "girl", "chick"):
        sex_option = "Ms."
    age_option = input("AGE: ")
    
    global player
    player = Player(name_option, surname_option, sex_option, age_option)
    time.sleep(1)
    print("\n")
    print("We were really impressed with your resume {} {}.".format(player.sex.title(),
                                                                    player.surname.title()))
    print("""\nWe decided we would like to offer you a position of Hazadrville's
Sheriff. Do you accept the offer?""")
    time.sleep(1)
    start()


def start():
    option = str(input("(Y/n): "))
    if option.lower() == "y":
        print("\n")
        print("Great! See you on Monday, Inspector!")
        time.sleep(2)
        os.system("cls")
        time.sleep(2)
        intro()
    elif option.lower() == "n":
        sys.exit()
    else:
        start()


def intro():
    print("2 years later...\n")
    time.sleep(2)
    os.system("cls")
    print("[SUNDAY, 1st of July, 07:21:30]\n")
    time.sleep(3)
    print("""You look through the window in you kitchen taking a sip of your
favourite tea. It's a lovely morning. And Hazardville is a lovely
town. Not even once during those two years you regretted your decision
about moving out from Seattle. Why would you? Nothing ever happened
here and you're a lazy """, end='')
    print('bastard' if player.sex == "Mr." else 'bitch', end='')
    print(""" with absolutely no ambition to be a
good cop.""")


prompt_for_name()

# to be continued #
