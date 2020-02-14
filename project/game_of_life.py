from sys import argv
import copy
###############################################################################
#                           5. Printing the graph!                           #
###############################################################################
def PrintThatGraph(graph):
    """This function prints the game's graph & converts 0s to '-'s and 1s to 'X's
        :param graph: A matrix of 0s and 1s
        :type graph: A series of lists in a list. Created using GraphGenerator() and altered during TheMainGame().
        :return: prints a graph of 'X's and '-'s
        :rtype: a list with 2400 elements (by default)
    """
    c=0
    i=0
    prettygraph=copy.deepcopy(graph) #If you don't make a copy, the gamegraph
    for c in range(30):              #will also be modified
        d=0
        for d in range(80):
            if prettygraph[c][d]==1:
                prettygraph[c][d]='X'
            else:
                prettygraph[c][d]='-'
        c+=1
    e=0
    for e in range(30): #This loop is going to join the cells and print
        f=0             #the boardgame to the terminal
        for f in range(80):
            print(prettygraph[e][f],end="")
            f+=1
        print('')
        e+=1
    print('\n') #IDK I think a newline between rounds makes it look nicer.
    i+=1

###############################################################################
#                           4. Deterimine who dies                            #
###############################################################################
def TheMainGame(gamegraph):
    """This function determines live cells and dead cells.

        The function determines if a cell is alive based on its neighbors following the rules outlined
        in Conway's Game of life. The function probably uses too many steps, but eh I tried ¯\_(ツ)_/¯
        :param gamegraph: A matrix of 0s and 1s
        :type gamegraph: A series of lists in a list. Formated with live/dead cells Created using life()
        :return: A new graph containing the survivors of the check -- new dead and alive cells.
        :rtype: a series of lists within a list
    """
    rounds=argv[1]                         #as implied by the name
    a=0
    i=0
    tempgraph=copy.deepcopy(gamegraph)
    j=0
    for i in range(int(rounds)):
        a=0
        for a in range(30): #Going to determine who is dead and who is alive
            if i==0: #before we begin, need to print the first map
                PrintThatGraph(gamegraph)
                i+=1
            else:
                b=0
                for b in range(80):
                    if a==0 and b==0:
                        neighborhood=0
                        below=a+1
                        right=b+1
                        neighborhood=int(gamegraph[int(below)][int(right)])+int(gamegraph[int(below)][int(b)])+int(gamegraph[int(a)][int(right)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    elif b==79 and a==0:
                        neighborhood=0
                        below=a+1
                        left=b-1
                        neighborhood=int(gamegraph[int(below)][int(left)])+int(gamegraph[int(below)][int(b)])+int(gamegraph[int(a)][int(left)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    elif a==0 and b>0 and b<79:
                        neighborhood=0
                        below=a+1
                        right=b+1
                        left=b-1
                        neighborhood=int(gamegraph[int(below)][int(left)])+int(gamegraph[int(below)][int(b)])+int(gamegraph[int(a)][int(left)])+neighborhood+int(gamegraph[int(below)][int(right)])+int(gamegraph[int(a)][int(right)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    elif a==29 and b==0:
                        neighborhood=0
                        above=a-1
                        right=b+1
                        neighborhood=int(gamegraph[int(above)][int(right)])+int(gamegraph[int(above)][int(b)])+int(gamegraph[int(a)][int(right)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    elif b==79 and a==29:
                        neighborhood=0
                        above=a-1
                        left=b-1
                        neighborhood=int(gamegraph[int(above)][int(left)])+int(gamegraph[int(above)][int(b)])+int(gamegraph[int(a)][int(left)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    elif a==29 and b<79 and b>0:
                        neighborhood=0
                        above=a-1
                        right=b+1
                        left=b-1
                        neighborhood=int(gamegraph[int(above)][int(left)])+int(gamegraph[int(above)][int(b)])+int(gamegraph[int(a)][int(left)])+int(gamegraph[int(above)][int(right)])+int(gamegraph[int(a)][int(right)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    elif b==0 and a<29 and a>0:
                        neighborhood=0
                        above=a-1
                        below=a+1
                        right=b+1
                        neighborhood=int(gamegraph[int(above)][int(right)])+int(gamegraph[int(above)][int(b)])+int(gamegraph[int(a)][int(right)])+int(gamegraph[int(below)][int(right)])+int(gamegraph[int(below)][int(b)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    elif b==79 and a<29 and a>0:
                        neighborhood=0
                        above=a-1
                        below=a+1
                        left=b-1
                        neighborhood=int(gamegraph[int(above)][int(left)])+int(gamegraph[int(above)][int(b)])+int(gamegraph[int(a)][int(left)])+int(gamegraph[int(below)][int(left)])+int(gamegraph[int(below)][int(b)])
                        if gamegraph[a][b]==1 and neighborhood<2:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==1 and neighborhood==2:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood==3:
                            tempgraph[a][b]=1
                        elif gamegraph[a][b]==1 and neighborhood>3:
                            tempgraph[a][b]=0
                        elif gamegraph[a][b]==0 and neighborhood==3:
                            tempgraph[a][b]=1
                        else:
                            pass
                    else:
                        neighborhood=0
                        neighborhood=gamegraph[a+1][b]+gamegraph[a-1][b]+gamegraph[a+1][b+1]+gamegraph[a-1][b+1]+gamegraph[a+1][b-1]+gamegraph[a-1][b-1]+gamegraph[a][b-1]+gamegraph[a][b+1]
                        if gamegraph[a][b]==1:
                            if neighborhood==2:
                                tempgraph[a][b]=int(1)
                            elif neighborhood==3:
                                tempgraph[a][b]=int(1)
                            elif neighborhood<2:
                                tempgraph[a][b]=int(0)
                            else:
                                tempgraph[a][b]=int(0)
                        else:
                            if neighborhood==3:
                                tempgraph[a][b]=int(1)
                            else:
                                pass
        gamegraph=copy.deepcopy(tempgraph)
        PrintThatGraph(gamegraph)
    PrintThatGraph(gamegraph)

################################################################################
#                       3. Bringing the graph to life!                         #
################################################################################
def life(gamegraph,formatedcoords): #This function places initial live cells
    """This function places initial live cells.

       This takes formated coordinats. These are then used to convert dead cells (0s) to
       live cells (1s)
       :param gamegraph: A matrix of 0s and 1s
       :type gamegraph: A series of lists in a list. Formated with dead cells Created using GraphGenerator()
       :param formatedcoords: A matrix of coordinates.
       :type formatedcoords: A series of lists that each correspond to a cell that is alive.
       :return: A new graph containing live cells corresponding to the users coordinates
       :rtype: a series of lists within a list\
    """
    a=0
    while a<len(formatedcoords): #Places initial live cells
        b=formatedcoords[a][0]
        b=int(b)-1   #by assigning 1s to live cells
        c=formatedcoords[a][1]
        c=int(c)-1
        gamegraph[int(b)][int(c)]=1
        a+=1
    TheMainGame(gamegraph)
################################################################################
#                    2. Formating the user's coordinates!                      #
################################################################################
def formatcoords(gamegraph): #function that input coordinates for future use
    """This function takes a list of coordinates and formats them for later use.

        Since the user's input includes ':' the function removes this, and stores the coordinates each as a list within a larger list
        Since python reads things starting at 0, 1 is subtracted from each coordinate so that the coordinates are places as expected
        :param gamegraph: a matrix of 0s and 1s
        :type gamegraph: a series of lists within a list
        :param coordinates: Command line input coordidinates
        :type coordinates: a string of numbers seperated by a ':'
        :return: coordinates that are formated for future use
        :rtype: each pair of coordinates make up one list in a larger list of all coordinates
    """
    coordinates=argv[2:]#Allows user to input as many coordinates as they'd like
    formatedcoords=[]
    z=0
    while z<len(coordinates):
        formatedcoords.append(coordinates[z].split(sep=':')) #removes : from coordinates
        z+=1
    z=0
    while z<len(formatedcoords):
        formatedcoords[z][0]=int(formatedcoords[z][0])+1
        formatedcoords[z][1]=int(formatedcoords[z][1])+1
        z+=1
    print(formatedcoords)
    life(gamegraph,formatedcoords)
################################################################################
#                            1. Generating the graph!                          #
################################################################################
def GraphGenerator(row,col): #function to generate the graph
    """This function generates the graph based off of user input
        In theory, these would be arguements, but I don't know how to set defaults in python
        :param row: The number of rows for the game grid
        :type row: Integer
        :param col: The number of columns for the game grid
        :type col: Integer
        :return: a matrix full of 0s with the deminsions provided from parameters
        :rtype: list within  a list
    """
    gamegraph=[0]*row #0s will repersent dead cells in this game
    for i in range(row):
        gamegraph[i]=[0]*int(col)
    formatcoords(gamegraph)
###############################################################################
#                                                                             #
###############################################################################
GraphGenerator(30,80) #In theory, you could set this as a user specified input
                      #But I don't know how to set defaults in python
