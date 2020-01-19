print("EXERCISE 5")
print(" ")
name='Zed A. Shaw'
age=35 #not a lie
height=74 #inches
weight=180 #lbs
height_cm=height*2.54
weight_kg=weight/2.205
eyes='Blue'
teeth='White'
hair='Brown'
print(f"Let's talk about {name}.")
print(f"He's {height} inches or {height_cm} cm tall")
print(f"He's {weight} pounds or {weight_kg} kg heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
#this line is tricky, try to get it exactly right
total=age+height+weight
total_metric=age+height_cm+weight_kg
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print (f"Alternatively, we could add the metric units for a sum of {total_metric}.")

