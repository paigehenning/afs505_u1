def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheese!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
print("We can give the function numbers directly:")
cheese_and_crackers(20,30)
print("OR, we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

print("Now, here is my uncreative study drill\n")
def I_am_not_creative(invited,coming,crashing,blankets):
	print(f"We can't have a party, without guests and blankets!")
	print(f"You have invited {invited} guests, only {coming} are coming")
	print(f"You have {blankets} blankets, I hope that's enough")
	print(f"Oh no! You have {crashing} party crashers! Bring out the spare blankets!\n")
print("First I will just give the function numbers directly:\n")
I_am_not_creative(10,5,2,200)
print("Now I guess I will assign the coming and crashing:\n")
coming_defined=10
crashing_defined=20
I_am_not_creative(10,coming_defined,crashing_defined,100000000)
print("Now I will ensure they have enough blankets:\n")
blankets_enough=coming_defined+crashing_defined
I_am_not_creative(20,coming_defined,crashing_defined,blankets_enough)
print("Now the poor guy won't have enough blankets(just doing math):\n")
I_am_not_creative(50,coming_defined,crashing_defined,40-coming_defined-crashing_defined)

I_am_not_creative(25,10,4,5*20/10)
I_am_not_creative(2^7,60/30*2,10,30)
I_am_not_creative(coming_defined+crashing_defined,coming_defined,crashing_defined^2,20)

print("I am running out of things to do, so I am giving up after only running the command 7 
ways")
