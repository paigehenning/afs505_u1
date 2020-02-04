from sys import exit
import random
def battle():
    print("Dramatic music starts playing")
    print("College student throws out Rattatta")
    Rattatta=30
    Bulbasaur=40
    while True:
        print("What attack do you use?")
        print("1. Vine whip")
        print("2. Tail whip")
        print("3. Tackle")
        choice=input("> ")
        print(" ")
        print(" ")
        if choice=="1":
            number=random.uniform(2,10)
            Rattatta-=number
            print(f"Rattatta takes {number} damage")
            number=random.uniform(2,6)
            Bulbasaur-=number
            print(f"Rattatta strikes. Bulbasaur takes {number} damage")
            if Bulbasaur<=0:
                dead("You fainted, better luck next time!")
            elif Rattatta<=0:
                dead("You won! You have won the game! Congrats!")
            else:
                {}
        elif choice=="2":
            print("Rattatta's defense falls")
            number=random.uniform(2,6)
            Bulbasaur-=number
            print(f"Rattatta strikes. Bulbasaur takes {number} damage")
            if Bulbasaur<=0:
                dead("You fainted, better luck next time!")
            elif Rattatta<=0:
                dead("You won! You have won the game! Congrats! ٩(˘◡˘)۶")
            else:{}
        elif choice=="3":
            number=random.uniform(2,6)
            Rattatta-=number
            print(f"Rattatta takes {number} damage")
            number=random.uniform(2,6)
            Bulbasaur-=number
            print(f"Rattatta strikes. Bulbasaur takes {number} damage")
            if Bulbasaur<=0:
                dead("You fainted, better luck next time!")
            elif Rattatta<=0:
                dead("You won! You have won the game! Congrats!")
            else:
                {}
        else:
            print("Bulbasaur is confused. He looks at you for a command")



def bulbasaur():
    print("You leave the office with your brand new bulbasaur")
    print("While walking, you run into a college student")
    print('"Hey, let\'s battle!"')
    print("Do you accept the challenge?")
    choice=input("> ")
    print(" ")
    print(" ")
    if choice=="yes" or choice=="Yes":
        battle()
    else:
        print("Hey! This is Pokemon! You\'re supposed to battle")
        dead("You fail as a Pokemon trainer because you refused to fight")

def lab():
    print("You walk into a lab and find a man sitting at a desk")
    print("The man notices you")
    print(f'"Greetings! You must be {name}"')
    print('"Here in the city of Pullman, we all have pet Pokemon"')
    print('"Your mother has sent you here to recieve your first Pokemon"')
    print(" ")
    print(" ")
    print(" ")
    print('"Which will you pick?"')
    print('"The grass type Bulbasaur"')
    print('"The fire type Charmander"')
    print('"Or the water type Squirtle?"')
    pokemon=input("> ")
    print(" ")
    print(" ")
    print(" ")
    if pokemon=="Charmander" or pokemon=="charmander":
        print("You pick Charmander!")
        dead("I am too lazy to write a storyline for every pokemon. hint pick bulbasaur")
    elif pokemon=="Squirtle" or pokemon=="squirtle":
        print("You pick Squirtle!")
        dead("I am too lazy to write a storyline for every pokemon. hint pick bulbasaur")
    elif pokemon=="Bulbasaur" or pokemon=="bulbasaur":
        print("You pick Bulbasaur!")
        bulbasaur()
    else:
        print('"Wow, looks like you can\' decide. How about you take this Pikachu?"')
        print("Do you take the Pikachu?")
        pikachu=input("> ")
        if pikachu=="yes" or pikachu=="Yes":
            print("You accept Pikachu as a starter")
            dead("I am too lazy to write a storyline for every pokemon. hint pick bulbasaur")
        else:
            dead("You decide not to take the Pikachu, your adventure ends here.")

def intro():
    print("You wake up in your new bedroom.")
    print("You walk downstairs to find your mom in the kitchen.")
    print(f'"Good morning honey. How did you sleep?"')
    print("1.Ok")
    print("2.Great")
    print("3. Bad")
    choice=input("> ")
    if choice=="1" or choice=="2":
        print('"That is good to hear. There were a bunch of Pidgeys in the yard earlier"')
    elif choice=="3":
        print('"Hopefully, you didn\'t have that dream about the Gengar again!"')
    else:
        print("Please pick 1,2, or 3")
    print('"There is a professor who wants to meet you, Dr. Ficklin"')
    print('"You should hurry along and go meet him"')
    print("Do you leave or stay at home?")
    choice=input("> ")
    if "leave" in choice:
        lab()
    else:
        dead("You decide to stay home. Your adventure ends here")

def stats():
    print("Are you a boy or a girl?")
    sex=input("> ")
    if sex=="girl":
        print(f"Okay, you\'re a {sex}. Now what\'s your name?")
        name()
    elif sex=="boy":
        print(f"Okay, you\'re a {sex}. Now what\'s your name?")
        name()
    else:
        print("For the sake of staying true to the Pokemon franchise, try again")
        stats()
def name():
    name=input("> ")
    if len(name)>0:
        print(f"Nice to meet you {name}")
        intro()
    else:
        print("Please enter your name")

def dead(why):
    print(why)
    print("Please don't tell Nitendo I plagiarized Pokemon")
    exit(0)
def start():
    print("You have just moved to Pullman, WA with your mother.")
    print("Your father has never been in the picture, so we won't address him")
    stats()
start()
