
numbers=[]
def ex33(start,stop,increments):
    print(f"This while loop starts at {start}")
    print(f"It will increase by {increments}")
    print(f"And it will stop when i less than or equal to {stop}")
    print(" ")
    i=start
#    while i<=stop:
#        print(f"At the top i is {i}")
#        numbers.append(i)
#        i+=increments
#        print("Numbers now: ",numbers)
#        print(f"At the bottom i is {i}")
#        print("The numbers: ")
#        for num in numbers:
#            print(num)
    for i in range(start,stop,increments):
        numbers.append(i)
    print(numbers)


ex33(1,20,3)
