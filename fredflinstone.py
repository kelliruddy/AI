import time

myBoard = []
movesPossible = []
coordinates ={}
alreadyBeen = ()
myDict =[]
currPosition ={}
validWords =[]

#get the beginning time in order to check how long execution took
start = time.time()

#Method to load in the game board given a text file
def loadBoard(filename):
    f = open(filename, 'r')
    for line in f.readlines():
        line.strip()
        myBoard.append(line.split())
        line.strip(' ')
    f.close()
    return myBoard

#Print out the board in NxN matrix
def printBoard(myBoard):
    for row in myBoard:
       print(' '.join(row))

#Generate all of the possible next moves based off of a given coordinate
def possibleMoves(coordinates,myBoard):
    x,y = coordinates
    possible = {}

    boardLength = len(myBoard)

    moves = [(x-1,y),(x+1,y),(x-1,y+1),(x+1,y+1),(x+1,y-1),(x,y-1),(x,y+1),(x-1,y-1)]

    possible[coordinates] = [p for p in moves if 0<= p[0] <boardLength and 0<p[1] < boardLength]

    movesPossible = possible[coordinates]
    #print(movesPossible)
    return possible


def legalMoves(movesPossible,alreadyBeen):
    #list to store all of the legal moves possible
    legalMoves = ()

    #for every coordinate in movesPossible
    for i in range(len(movesPossible)):
        #if first coordinate in movesPossible is not in alreadyBeen then add it to legalMoves
        if movesPossible[i] not in alreadyBeen:
            legalMoves = legalMoves + movesPossible[i]


#Method to import the given dictionary and store
def importDictionary(file):
    f = open(file, 'r')
    for line in f.readlines():
        myDict.append(line.split())
    f.close()
    return myDict

#
def examineState(myBoard,currPosition,path,myDict):
    x,y = currPosition


    #add the first letter to the word list
    word = (myBoard[x][y])

    for i in range(len(path)):
        k,m = path[i]
        word = word + (myBoard[k][m])

    word = word + (myBoard[x][y])
    word = (word[1:]).lower()
    print(word)

    for i in range(len(myDict)):
         if word in myDict[i]:
            print("Yes")


#should search every path possible and store the valid words
def wordsFound(myBoard, myDict,path):
    #check if the segment of word found is in dictionary, if not break else keep exploring

    #if the word is in the dictionary then add it to the valid words list

    #check if there is another move possible from current position and then recursively call wordsFound



#print out how long the program took to execute
def howLong():
    print("Found XXXXX words in ", time.time() - start)













def main():
    loadBoard('blah.txt')
    printBoard(myBoard)


    # possibleMoves((2,2),myBoard)
    # legalMoves(possibleMoves((2,2),myBoard),((0,0),(1,1),(2,2),(3,3)))
    importDictionary('words.txt')
    # examineState(myBoard,(3,1),((0,1),(1,0),(1,1),(2,1)), myDict)

    wordsFound(myBoard, myDict)
    howLong()


main()

