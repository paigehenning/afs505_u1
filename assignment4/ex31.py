print("""You enter a dark room with three doors.
Do you go through door #1, door #2, or door #3?""")
door=input("> ")
if door== "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear=input("> ")

    if bear=="1":
        print("The bear eats your face off. Good job!")
    elif bear=="2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door=="2":
    print("You sate into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    instanity=input("> ")
    if instanity=="1" or instanity=="2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of much.")
        print("Good job!")
elif door=="3":
    print("You are suddenly in your childhood bedroom")
    print("What do you do?")
    print("1. Reminisce")
    print("2. Go looking for your parent(s)")
    print("3. Play Pokemon Saphire")
    print("4. Try to go back through the door")
    childhood=input("> ")
    if childhood == "1":
        print("You start to think about how great of a cook your parent was")
        print("You begin thinking about how much fun you had playing Pokemon")
        print("You realize you haven't felt true happiness in a long time")
        print("You cry. Good job!")
    elif childhood == "2":
        print("You run downstairs looking for your parent(s)")
        print("The house is empty")
        print("Where do you go now?")
        print("1. To the backyard")
        print("2. To their bedroom")
        parent=input("> ")
        if parent == "1":
                print("You run outside")
                print("As you step onto the patio the sky begins to crumble")
                print("The ground begins to shake violently")
                print("The house is melting!!!")
                print("You broke the simulation")
                print("Good job!")
        elif parent=="2":
            print("You walk in on your parent changing")
            print("You die of embarassement. Good job!")
        else:
            print("You suddenly wake up at home. Wow this was all a dream!")
    elif childhood=="3":
        print("You start a new save")
        print("What starter do you pick?")
        print("1. The grass type Treecko")
        print("2. The fire type Torchick")
        print("3. The water type Mudkip")
        pokemon=input("> ")
        if pokemon=="1" or pokemon=="2":
            print("You made the wrong choice")
            print("No matter how hard you try, your rival beats you")
        elif pokemon=="3":
            print("Oh!!! Your mudkip is pink!")
            print("A shiny mudkip!! How lucky!")
            print("You play pokemon and have a great time!")
        else:
            print("That's not a choice")
            print("your gameboy breaks")
            print("Better luck next time")
    elif childhood=="4":
        print("Oh no you can't get out")
        print("Suddenly, you feel weird")
        print("You look down at your hands")
        print("They're shrinking to child sized hands")
        print("You run to the bathroom and look in the mirror")
        print("A child looks back at you")
        print("Guess you are reliving your childhood")
    else:
        print("Looks like you can't follow directions")
        print("You explode")
else:
    print("You stumble around and fall on a knife and die. Good job!")
