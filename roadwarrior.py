from GraphViz import *


class SearchNode():
    openList = []

    # Initialize variables and list to hold map
    def __init__(self, filename):
        self.value = 0
        self.label = ''
        self.file = open(filename,'r')
        self.map = []
        self.successors = []
        for line in self.file.readlines():
            line.strip()
            self.map.append(line)
        self.file.close()


    # Method to print the map in more organized way
    def printMap(self):
        for row in self.map:
            print(''.join(row))

    # Set the starting node and the desired end node
    def setStartAndGoal(self,start,goal):
        start = start
        goal = goal

        return start,goal


    # Method to get and show the open list given by the map
    def showOpen(self,openList):
        openList.append(1)
        print (openList)
        return openList












        # # Get the label value for each node in the text file
        # for list in self.map:
        #     self.label = (list[2])
        #     self.value = (list[11])
        #
        #     # Check to see if label is 2 letters and if it is, add it to label
        #     if list[3] != "'":
        #         self.label = self.label +list[3]
        #
        #     # Get value of each node
        #     if list[12] != ' ':
        #         self.value = self.value + list[12]
        #     if list[13] != ',' or list[13] != ' ':
        #         self.value = self.value + list[13]
        #     if list[14] != ',' or list[14] != ' ':
        #         self.value = self.value + list[14]
        #
        #     #add all labels and values to the open list
        #     self.openList.append((self.label, self.value))
        # print(self.openList)

    # Get the successors/children of node U - check the label and grab its corresponding neighbor
    def getSuccessors(self,openList):
        print(openList)

        #if self.value = U.....get the corresponding next letter
        if self.label == 'U':
            # Grab its successor and add to successors list
            print('')


    # Method to insert the successors into the open list
    def insert(self):
        for i in range(len(self.successors)):
            self.openList.append(self.successors[i])



x = SearchNode('30Node.txt')
x.getSuccessors()



# Graph map from text file
x=GraphViz()  # make yourself a new visualizer
x.loadGraphFromFile('30Node.txt')  # load it up from a map file
x.plot()  # make the plot of the road map appear
x.markStart('U')  # mark starting node A
x.markGoal('T')   # mark 'D' as a goal node
plt.pause(1000)