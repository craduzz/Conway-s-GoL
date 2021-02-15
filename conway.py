"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]


def configLib(selection):
    """Library of all the configurations templates in the document"""
    o = 0
    x = 255

    # Still lives

    blockCell = np.array([[o, o, o, o],  #4x4
                          [o, x, x, o],
                          [o, x, x, o],
                          [o, o, o, o]])

    beehiveCell = np.array([[o, o, o, o, o, o],   #6x5
                            [o, o, x, x, o, o],
                            [o, x, o, o, x, o],
                            [o, o, x, x, o, o],
                            [o, o, o, o, o, o]])

    loafCell = np.array([[o, o, o, o, o, o],  #6x6
                         [o, o, x, x, o, o],
                         [o, x, o, o, x, o],
                         [o, o, x, o, x, o],
                         [o, o, o, x, o, o],
                         [o, o, o, o, o, o]])

    boatCell = np.array([[o, o, o, o, o],  #5x5
                         [o, x, x, o, o],
                         [o, x, o, x, o],
                         [o, o, x, o, o],
                         [o, o, o, o, o]])

    tubCell = np.array([[o, o, o, o, o],  #5x5
                        [o, o, x, o, o],
                        [o, x, o, x, o],
                        [o, o, x, o, o],
                        [o, o, o, o, o]])


    # Oscilators

    blinkerCell1 = np.array([[o, o, o],  # 3x5
                             [o, x, o],
                             [o, x, o],
                             [o, x, o],
                             [o, o, o]])

    blinkerCell2 = np.array([[o, o, o, o, o],  #5x3
                             [o, x, x, x, o],
                             [o, o, o, o, o]])

    toadCell1 = np.array([[o, o, o, o, o, o],  # 6x6
                          [o, o, o, x, o, o],
                          [o, x, o, o, x, o],
                          [o, x, o, o, x, o],
                          [o, o, x, o, o, o],
                          [o, o, o, o, o, o]])

    toadCell2 = np.array([[o, o, o, o, o, o],  # 6x5
                          [o, o, x, x, x, o],
                          [o, x, x, x, o, o],
                          [o, o, o, o, o, o]])

    beaconCell1 = np.array([[o, o, o, o, o, o],  # 6x6
                            [o, x, x, o, o, o],
                            [o, x, x, o, o, o],
                            [o, o, o, x, x, o],
                            [o, o, o, x, x, o],
                            [o, o, o, o, o, o]])

    beaconCell2 = np.array([[o, o, o, o, o, o],  # 6x6
                            [o, x, x, o, o, o],
                            [o, x, o, o, o, o],
                            [o, o, o, o, x, o],
                            [o, o, o, x, x, o],
                            [o, o, o, o, o, o]])

    # Gliders

    gliderCell1 = np.array([[o, o, o, o, o],  # 5x5
                            [o, o, x, o, o],
                            [o, o, o, x, o],
                            [o, x, x, x, o],
                            [o, o, o, o, o]])

    gliderCell2 = np.array([[o, o, o, o, o],  # 5x5
                            [o, x, o, x, o],
                            [o, o, x, x, o],
                            [o, o, x, o, o],
                            [o, o, o, o, o]])

    gliderCell3 = np.array([[o, o, o, o, o],  # 5x5
                            [o, o, o, x, o],
                            [o, x, o, x, o],
                            [o, o, x, x, o],
                            [o, o, o, o, o]])

    gliderCell4 = np.array([[o, o, o, o, o],  # 5x5
                            [o, x, o, o, o],
                            [o, o, x, x, o],
                            [o, x, x, o, o],
                            [o, o, o, o, o]])

    lWSpaceship1 = np.array([[o, o, o, o, o, o, o],  # 7x6
                             [o, x, o, o, x, o, o],
                             [o, o, o, o, o, x, o],
                             [o, x, o, o, o, x, o],
                             [o, o, x, x, x, x, o],
                             [o, o, o, o, o, o, o]])

    lWSpaceship2 = np.array([[o, o, o, o, o, o, o],  # 7x6
                             [o, o, o, x, x, o, o],
                             [o, x, x, o, x, x, o],
                             [o, x, x, x, x, o, o],
                             [o, o, x, x, o, o, o],
                             [o, o, o, o, o, o, o]])

    lWSpaceship3 = np.array([[o, o, o, o, o, o, o],  # 7x6
                             [o, o, x, x, x, x, o],
                             [o, x, o, o, o, x, o],
                             [o, o, o, o, o, x, o],
                             [o, x, o, o, x, o, o],
                             [o, o, o, o, o, o, o]])

    lWSpaceship4 = np.array([[o, o, o, o, o, o, o],  # 7x6
                             [o, o, x, x, o, o, o],
                             [o, x, x, x, x, o, o],
                             [o, x, x, o, x, x, o],
                             [o, o, o, x, x, o, o],
                             [o, o, o, o, o, o, o]])

    if selection == 1:
        return blockCell
    elif selection == 2:
        return beehiveCell
    elif selection == 3:
        return loafCell
    elif selection == 4:
        return boatCell
    elif selection == 5:
        return tubCell
    # -------------------------------------------------------
    elif selection == 6:
        return blinkerCell1
    elif selection == 7:
        return blinkerCell2
    elif selection == 8:
        return toadCell1
    elif selection == 9:
        return toadCell2
    elif selection == 10:
        return beaconCell1
    elif selection == 11:
        return beaconCell2
    # ---------------------------------------------------------
    elif selection == 12:
        return gliderCell1
    elif selection == 13:
        return gliderCell2
    elif selection == 14:
        return gliderCell3
    elif selection == 15:
        return gliderCell4

    elif selection == 16:
        return lWSpaceship1
    elif selection == 17:
        return lWSpaceship2
    elif selection == 18:
        return lWSpaceship3
    elif selection == 19:
        return lWSpaceship4


def ruleOneTwoThree(oldGrid, newGrid, i, j):
    """apply the first, second and third rule of Conway's GoL"""
    # set the bound of the array for validation
    min = 0
    max = len(oldGrid[i])

    # initialize the neighbors counter
    liveNeighbours = 0

    # initialize the size of the neighborhood search
    neighborhood = np.array([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]])

    x = -1
    y = -1

    # Search the neighbors of a predefined size
    for row in neighborhood:
        for value in row:

            # validate that the search is not out of bounds or in the center
            if (x + i) >= min and (x+i) < max:
                if(y + j) >= min and (y+j) < max:
                    if x != 0 or y != 0:

                        # if a neighbor is found count it
                        if oldGrid[x+i][y+j] == 255:
                            liveNeighbours += 1

            y += 1
        x += 1
        y = -1

    # if there are 1 or less neighbors or 4 or more neighbors kill the cell
    if liveNeighbours < 2 or liveNeighbours >= 4:
        newGrid[i][j] = 0
        return newGrid

    # else leave the cell untouched
    else:
        return newGrid


def ruleFour(oldGrid, newGrid,i,j):
    """Apply the fourth rule of Conway's GoL"""
    # set the bound of the array for validation
    min = 0
    max = len(oldGrid[i])

    # initialize the neighbors counter
    liveNeighbours = 0

    # initialize the size of the neighborhood search
    neighborhood = np.array([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]])

    x = -1
    y = -1
    # Search the neighbors of a predefined size
    for row in neighborhood:
        for value in row:

            # validate that the search is not out of bounds or in the center
            if (x + i) >= min and (x+i) < max:
                if (y + j) >= min and (y+j) < max:
                    if x != 0 or y != 0:

                        # if a neighbor is found count it
                        if oldGrid[x+i][y+j] == 255:
                            liveNeighbours += 1

            y += 1
        x += 1
        y = -1

    # if there are exaclty 3 neigbors make a live cell
    if liveNeighbours == 3:
        newGrid[i][j] = 255
        return newGrid

    # else leave it as it is
    else:
        return newGrid


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.3, 0.7]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255],
                       [255,  0, 255],
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def addShape(i, j, grid):
    """Function to test custom shapes to insert in a specified location"""
    o = 0
    x = 255

    shape = np.array([[x, x, x],
                      [x, x, x],
                      [x, x, x]])

    shape2 = np.array([[o, o, o, o],
                       [x, o, x, o],
                       [o, x, x, o],
                       [o, x, o, o]])

    grid[i:i+4, j:j+4] = shape2


def searchConfig(grid, i, j):
    """Searches if the cell found matches any of the configurations"""

    # Saves the original value of j
    jBase = j

    # initialize the counters for the loops
    a = 0
    b = 0

    # flag that says if  configurations has been found
    foundConfig = True

    # Compares all 19 configurations that are in the document
    for x in range(1,20):
        # gets the template of the configurations in the range
        tmpGrid = configLib(x)

        # column value correction for certain configurations
        if x == 2 or x == 3 or x == 5 or x == 9 or x == 12 or x == 18 or x == 19:
            j -= 1
        elif x == 8 or x == 14 or x == 17:
            j -= 2
        else:
            j = jBase

        # compares cell by cell the live cell found with the templates to see if there is a match
        for row in tmpGrid:
            for value in row:
                # Validate that the search is not out of index
                if (i+a) < len(grid) and (j+b) < len(grid):
                    valueOfGrid = int(grid[i+a][j+b])
                else:
                    foundConfig = False
                    break

                # when the comparison fails stop the comparison and move to the next configuration template
                if valueOfGrid != value:
                    foundConfig = False
                    break

                b += 1
            a += 1
            b = 0
            if foundConfig == False:
                break
        a = 0
        # Return the number associated to the configurations
        if foundConfig == True:
            return x
        else:
            foundConfig = True
    # If nothing was found return a negative value
    return -1


def getConfigName(configNum):
    """Return the name of the configurations according to the obtained number"""

    if configNum == 1:
        return "Block: "
    elif configNum == 2:
        return "Beehive: "
    elif configNum == 3:
        return "Loaf: "
    elif configNum == 4:
        return "Boat: "
    elif configNum == 5:
        return "Tub: "
    elif configNum == 6 or configNum == 7:
        return "Blinker: "
    elif configNum == 8 or configNum == 9:
        return "Toad: "
    elif configNum == 10 or configNum == 11:
        return "Beacon: "
    elif configNum == 12 or configNum == 13 or configNum == 14 or configNum == 15:
        return "Glider: "
    elif configNum == 16 or configNum == 17 or configNum == 18 or configNum == 19:
        return "Light-weight spaceship: "

def writeLog(listOfFoundConfig,frameNum):
    """Receives the list of the found configurations and the current generation to write them on the output log"""
    listHasValues = True

    # Open the output file and start writing the results
    log = open("generationsData.txt","a")
    log.write("------------------------------------------------------------------------------------------ \n")
    log.write("                              Generation: ")
    log.write(str(frameNum))
    log.write("\nConfigurations found: \n")

    # Writes the name of the configurations found and its amount
    while listHasValues:
        # gets the first configuration
        configNumber = listOfFoundConfig[0]
        # gets the amount of time its on the list
        configNumberAmount = listOfFoundConfig.count(listOfFoundConfig[0])
        # removes the configuration/s from the list so it won't be counted again
        listOfFoundConfig[:] = [config for config in listOfFoundConfig if config != listOfFoundConfig[0]]
        log.write(getConfigName(configNumber))
        log.write(str(configNumberAmount))
        log.write("\n")
        # if the list is empty finish the loop
        if not listOfFoundConfig:
            listHasValues = False
    log.write(" \n")


def update(frameNum, img, grid, N):
    # Create a grid n+2 size of the original grid
    configGrid = np.zeros((N + 2) * (N + 2)).reshape((N + 2), (N + 2))
    # Places the grid in the center of the n+2 grid
    configGrid[1:N+1,1:N+1] = grid

    # initialize the list of the configurations found
    listOfFoundConfig = []

    i = 0
    j = 0

    # loop to find all the live cells
    for row in grid:
        for cell in row:
            if cell == 255:
                # send the position of the cell found and the n+2 grid to see if there is a cell configuration
                numFound = searchConfig(configGrid, i, j)
                # if a configuration was found add it to a list
                if numFound > 0:
                    listOfFoundConfig.append(numFound)
            j += 1
        i += 1
        j = 0

    # sends the list and the current frame to the output log writer
    writeLog(listOfFoundConfig,frameNum)


    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()

    i = 0
    j = 0

    # Loop to move through every cell in the grid
    for row in newGrid:
        for cell in row:
            if cell == 255:
                ruleOneTwoThree(grid, newGrid, i, j)
            elif cell == 0:
                ruleFour(grid, newGrid, i, j)

            j += 1
        i += 1
        j = 0

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments

    log = open("generationsData.txt", "w")
    log.write("")
    log.close()

    # list of coordinates of live cells
    initialCells = []

    # open the input file
    inputFile = open("input.txt", "r")

    # read the lines of the input file
    for line in inputFile:

        # set grid size
        if "SIZE: " in line:
            tmp = line.replace("SIZE: ", "")
            N = int(tmp)

        # set the amount of generations
        elif "GENERATIONS: " in line:
            tmp = line.replace("GENERATIONS: ", "")
            Generations = int(tmp)

        elif "SPEED: " in line:
            tmp = line.replace("SPEED: ", "")
            updateInterval = int(tmp)

        else:
            coordinates = line.split()
            initialCells.append(coordinates)

    print(initialCells)
    # set animation update interval
    # declare grid
    grid = np.array([])

    # Uncomment to populate grid with random on/off - more off than on
    # grid = randomGrid(N)

    # Uncomment lines to see the "glider" demo
    # addGlider(1, 1, grid)
    # addShape(4,5,grid)

    # initialize the grid size
    grid = np.zeros(N*N).reshape(N, N)

    for position in initialCells :
        grid[int(position[0])][int(position[1])] = 255

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames=Generations,
                                  interval=updateInterval,
                                  save_count=50, repeat=False)

    plt.show()


# call main
if __name__ == '__main__':
    main()
