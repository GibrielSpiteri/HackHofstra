# class UI(object):

# Returns name of read in file
def getFilename():
    filename = input("What file would you like to use: ")
    return filename

def yes_no():
    while True:
        answer = input("?: ")
        if(answer.lower() == "y"):
            return True
        elif(answer.lower() == "n"):
            return False
        else:
            print("Invalid Input, please answer 'y' or 'n'.")

# Returns player decided move
def getPlayerMove(character):
    move = ""
    while move not in ("H", "Q", "W", "E", "A", "S", "D", "Z", "X", "C"):
        move = input("Player " + character + ", Please enter a move, use 'h' for help\n")
        move = move.upper()
        if move == "H":
            print("To enter a move press the corressponding: ")
            print("Q, W, E\nA, S, D\nZ, X, C")
            move = ""
        elif move in ("Q", "W", "E", "A", "S", "D", "Z", "X", "C"):
            if move == "Q":
                return (-1, -1)
            elif move == "W":
                return (0, -1)
            elif move == "E":
                return (1, -1)
            elif move == "A":
                return (-1, 0)
            elif move == "S":
                return (0, 0)
            elif move == "D":
                return (1, 0)
            elif move == "Z":
                return (-1, 1)
            elif move == "X":
                return (0, 1)
            else:
                return (1, 1)

        else:
            print("Invalid Input")


# Returns how many players are playing the game
def getNoPlayers(maxVal):
    players = 0
    print("How many players are there? Max #: {}".format(maxVal))
    while True:
        players = int(input(""))
        if players < 2 or players > maxVal:
            print("Invalid input, choose a number between 0 and {}.".format(max))
        else:
            return players

# Returns player decided starting spot
def getStartLocation(board):
    finishLine = board.finishline
    maxVal = len(finishLine)
    position = 0
    if maxVal == 1:
        startPoint = finishLine[0]
        return startPoint
    else:
        print("Choose a starting position between 1 and {}".format(maxVal))
        while True:
            position = int(input(""))
            if position < 0 or position > maxVal:
                print("Invalid Input,enter a number between 1 and {}".format(maxVal))
            else:
                startPoint = finishLine[position]
                del board.finishline[position]
                return startPoint