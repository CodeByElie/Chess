from chess import Chess

game = Chess()
game.initializeGame()

while not game.isCheckmate():
    game.draw()
    move = input("Next move : ")
    while(not game.move(move)):
        print("Incorrect move")
        move = input("Next move : ")
    