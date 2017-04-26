import UI

class Player(object):

    def __init__(self, coords, character):
        self.x = coords[0]  # tuples that store player location
        self.y = coords[1]
        self.coords = coords
        self.char = character
        self.vel = [0, 0]  # tuple used for velocity
        self.prevPosition = [0, 0]
        self.crashed = False
        self.skipturn = False
        self.laps = 2

    def ordered(self, x, y ,z):
        if x <= y and y <= z:
            return True
        elif x >= y and y >= z:
            return True
        else:
            return False

    # calculates the Players next position
    def movePlayer(self, move):
        self.prevPosition = [self.x, self.y]
        self.vel[0] += move[0]
        self.vel[1] += move[1]
        self.x += self.vel[0]
        self.y += self.vel[1]

    def inRange(self, value, domain):
        if domain[0] > domain[1]:
            return domain[0] >= value and value >= domain[1]
        else:
            return domain[0] <= value and value <= domain[1]

    def makeMove(self, board):
        board.direction = "^"
        if self.crashed == True and self.skipturn == True:
            print("Turn Skipped for crashing!")
            self.crashed = True
            self.skipturn = False
            return True

        elif self.crashed == True and self.skipturn == False:
            # get move from player
            nextMove = UI.getPlayerMove(self.char)
            # next velocity vector
            nextVel = [self.vel[0] + nextMove[0], self.vel[1] + nextMove[1]]
            # next position is equal to the old pos + the new velocity
            nextLoc = [self.x + nextVel[0], self.y + nextVel[1]]
            # check and correct for out of bounds
            if nextLoc[0] < 0:
                nextLoc = [0] + [nextLoc[1]]
            elif nextLoc[0] > board.dimensions[0]:
                nextLoc = [board.dimensions[0]] + [nextLoc[1]]
            if nextLoc[1] < 0:
                nextLoc = [nextLoc[0]] + [0]
            elif nextLoc[1] > board.dimensions[1]:
                nextLoc = [nextLoc[0]] + [board.dimensions[1]]
            # char of the next location
            nextLocChar = board.getCharAt(nextLoc)
            # if trying to run over another player, do not allow
            if nextLocChar.isupper():
                return False
            else:
                # all requirements met, make the move
                board.makeMove(self.coords, nextLoc)
                self.prevPosition = self.coords
                self.coords = nextLoc
                # calculate the slope of the line between the old and new location
                try:
                    slope = (self.prevPosition[1]-self.coords[1])/(self.coords[0]-self.prevPosition[0])
                except:
                    slope = 100
                # establish moveline parameters
                moveLine = (slope, self.coords[1] - slope*self.coords[0])
                # if finishline is horizontal
                if board.direction in ("^", "v"):
                    # if the y-values are around the finish
                    if self.ordered(self.prevPosition[1], board.y_range[0], self.coords[1]):
                        # calculate x-value of the moveline's intersection with the finish
                        try:
                            intersect = (board.y_range[0]-moveLine[1])/moveLine[0]
                        except:
                            intersect = 10000
                        # if the value lies in between the bounds of the finish:
                        # calculate wether to award or punish player
                        if self.inRange(intersect, board.x_range):
                            if board.direction == "^" and slope > 0:
                                self.laps -= 1
                            elif board.direction == "^" and slope < 0:
                                self.laps += 1
                            elif board.direction == "v" and slope < 0:
                                self.laps -= 1
                            else:
                                self.laps += 1
                # update parameters
                self.x = self.coords[0]
                self.y = self.coords[1]
                self.vel = nextVel
                # check for crashes
                if nextLocChar == "%":
                    self.vel = (0,0)
                else:
                    self.crashed = False

        else:
            nextMove = UI.getPlayerMove(self.char)
            nextVel = [self.vel[0] + nextMove[0], self.vel[1] + nextMove[1]]
            nextLoc = [self.x + nextVel[0], self.y + nextVel[1]]
            if nextLoc[0] < 0:
                nextLoc = [0] + [nextLoc[1]]
            elif nextLoc[0] > board.dimensions[0]:
                nextLoc = [board.dimensions[0]] + [nextLoc[1]]
            if nextLoc[1] < 0:
                nextLoc = [nextLoc[0]] + [0]
            elif nextLoc[1] > board.dimensions[1]:
                nextLoc = [nextLoc[0]] + [board.dimensions[1]]
            nextLocChar = board.getCharAt(nextLoc)
            if nextLocChar.isupper():
                return False
            board.makeMove(self.coords, nextLoc)
            self.prevPosition = self.coords
            self.coords = nextLoc
            try:
                slope = (self.prevPosition[1]-self.coords[1])/(self.coords[0]-self.prevPosition[0])
            except:
                slope = 100
            moveLine = (slope, self.coords[1] - slope*self.coords[0])
            if board.direction in ("^", "v"):
                if self.ordered(self.prevPosition[1], board.y_range[0], self.coords[1]):
                    intersect = (board.y_range[0]-moveLine[1])/moveLine[0]
                    if self.inRange(int(intersect), board.x_range):
                        if board.direction == "^" and slope > 0:
                            self.laps -= 1
                        elif board.direction == "^" and slope < 0:
                            self.laps += 1
                        elif board.direction == "v" and slope < 0:
                            self.laps -= 1
                        else:
                            self.laps += 1
            self.x = self.coords[0]
            self.y = self.coords[1]
            self.vel = nextVel
            if nextLocChar == "%":
                self.vel = (0, 0)
                self.crashed = True
                self.skipturn = True



# coord = [1, 2]
# moves = [1, 2]
# objects = Player(coord)
# print(objects.movePlayer(moves))
# print(objects.movePlayer(moves))
