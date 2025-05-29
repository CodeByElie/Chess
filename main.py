from chess import Chess

game = Chess()
game.initializeGame()

while True:
    game.draw()
    move = input("Next move : ")
    while(not game.move(move)):
        print("Incorrect move")
        move = input("Next move : ")
    if game.isCheck():
        print("CHECK")
    