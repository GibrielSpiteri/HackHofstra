import UI
import board
import player

def main():
	while True:
		run()
		while True:
			new_game = UI.yes_no()
			if(not new_game):
				break

def run():
	board = boardSetup()
	players = playerSetup(board)
	while True:
		board.printBoard()
		currPlayer = players[0]
		currPlayer.makeMove(board)
		if currPlayer.laps == 0:
			win(currPlayer)
			break
		players = players[1:] + [currPlayer]

def win(player):
	print("Player "+player.char+" wins!! COngratulations!\nPlay Again? (y/n)")

def boardSetup():
	filename = UI.getFilename()
	return board.Board(filename)

def playerSetup(board):
	players = []
	playerChars = ["X", "O", "U", "V", "W"]
	noPlayers = UI.getNoPlayers(len(board.finishline))
	for i in range(0, noPlayers):
		startLocation = UI.getStartLocation(board)
		newPlayer = player.Player(startLocation, playerChars[i])
		players = [newPlayer] + players
		board.placeChar(newPlayer.coords, newPlayer.char)
	return players

main()
