print("EXERCISE 8")
print(" ")
formatter="{} {} {} {}" #creates the variable formatter which conisistes of 4 variables
print(formatter.format(1,2,3,4)) #assigns values to the 4 variables
print(formatter.format("one","two","three","four")) #again assigning values
print(formatter.format(True,False,False,True)) #all of these are assigning values
print(formatter.format(formatter,formatter,formatter,formatter)) #same
print(formatter.format( #again this is the same. just assigning strings to the variables
    "I am not creative enough",
    "To come up with a poem or song about fear",
    "So I am just going to ramble",
    "About not being creative"
))
