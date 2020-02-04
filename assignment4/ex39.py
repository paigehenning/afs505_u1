states={
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI',
    'Washington':'WA',
    'Texas':'TX'
}
cities={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville',
    'TX':'Dallas'
}
people={
    'Bill Gates':'Washington',
    "George W Bush":"TX",
    'Lady Gaga':'NY',
    'Lynyrd Skynyrd':'Jacksonville'
}
cities['NY']='New York'
cities['OR']='Portland'
cities['WA']='Seattle'
print('-'*10)
print("NY State has: ",cities['NY'])
print("OR State has: ",cities['OR'])
print('-'*10)
print("Michigan's abbreviation is: ",states['Michigan'])
print("Florida's abbreviation is: ",states['Florida'])
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
print('-'*10)
state=states.get("Texas")
if not state:
    print("Sorry, no Texas.")
city=cities.get('TX', "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")
print('-'*10)
for people, state in list(people.items()):
    print(f"{people} is from {state}")
print("hmmm cannot figure out how to change the abbreviated states to their full name")
