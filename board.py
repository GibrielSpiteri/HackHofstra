class Board:
	def __init__(self, filename):
		self.trackFile = open(filename, 'r')
		self.trackString = self.trackFile.readline()
		self.linelength = len(self.trackString)
		self.trackString += self.trackFile.read()
		self.dimensions = (self.linelength-2, int((len(self.trackString)+1)/self.linelength))

		self.finishline = self.getFinishline()
		self.direction = "-"
		if self.finishline[0][0] == self.finishline[1][0]:
			self.y_range = [self.finishline[0][1], self.finishline[-1][1]]
			self.x_range = [self.finishline[0][0]]
		else:
			self.y_range = [self.finishline[0][1]]
			self.x_range = [self.finishline[0][0], self.finishline[-1][0]]

		self.vertMiddle = self.linelength/2
		self.horizMiddle = len(self.trackString)/(2*self.linelength)

	def getFinishline(self):
		finishline = []
		for i in range(0,len(self.trackString)):
			if self.trackString[i] in ("^", ">", "v", "<"):
				char = self.trackString[i]
				self.direction = char
				break
		if char in (">", "<"):
			finishline.append(self.getCoordsOf(i))
			i += self.linelength
			nextChar = self.trackString[i]
			while nextChar == char:
				finishline.append(self.getCoordsOf(i))
				i += self.linelength
				nextChar = self.trackString[i]
			return finishline
		else:
			finishline.append(self.getCoordsOf(i))
			i += 1
			nextChar = self.trackString[i]
			while nextChar == char:
				finishline.append(self.getCoordsOf(i))
				i += 1
				nextChar = self.trackString[i]
			return finishline

	def makeMove(self, fromCoords, toCoords):
		char = self.getCharAt(fromCoords)
		self.placeChar(toCoords, char)
		self.placeChar(fromCoords, char.lower())

	def placeChar(self, coords, player):
		index = self.getIndexOf(coords)
		self.trackString = self.trackString[:index] + player + self.trackString[index+1:]

	def printBoard(self):
		print(self.trackString)

	def getIndexOf(self, coords):
		return coords[1] * self.linelength + coords[0]

	def getCoordsOf(self, index):
		return (index % self.linelength, int(index / self.linelength))

	def getCharAt(self, coords):
		x = coords[0]
		y = coords[1]
		index = y * self.linelength + x
		return self.trackString[index]

# print(board.finishline)
# print(board.getCoordsOf(101))
# print(board.trackString)
# board.printboard()
# print(board.getCharAt((0,0)))
# print(board.getCharAt((3,3)))
# print(board.getCharAt((2,3)))