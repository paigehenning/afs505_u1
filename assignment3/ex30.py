people=50
cars=40
trucks=15
if cars>people:
    print("We should take the cars.")
elif cars<people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
if trucks>cars:
    print("That's too many trucks.")
elif trucks<cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
if people>trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's just stay home then.")
print("Can we all have a car or truck?")
if people<=cars:
    print("Everyone gets their own car")
elif people<=trucks:
    print("Everyone gets their own truck")
elif people<=trucks+cars:
    print("Everyone gets their own vehicle")
else:
    print("We have to share vehicles")
