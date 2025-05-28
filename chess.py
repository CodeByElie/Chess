
PIECES = {
    "BP" : "\u2659",
    "BB" : "\u2657",
    "BR" : "\u2656",
    "BQ" : "\u2655",
    "BK" : "\u2654",
    "WP" : "\u265f",
    "WN" : "\u265e",
    "WB" : "\u265d",
    "WR" : "\u265c",
    "WQ" : "\u265b",
    "WK" : "\u265a",
    "BN" : "\u2658",
    "WN" : "\u265e"
}

class Chess:
    def __init__(self):
        self.__gameboard = [[None for i in range(8)] for j in range(8)]

    def initializeGame(self):
        order = "RNBQKBNR"
        for i in range(0,8):
            self.__gameboard[1][i] = "WP"
            self.__gameboard[0][i] = "W"+order[i]
            self.__gameboard[6][i] = "BP"
            self.__gameboard[7][i] = "B"+order[i]
        print(self.__gameboard)
    
    def draw(self):
        print("-"*33)
        for i in range(8):
            for j in range(8):
                print(f"| {PIECES[self.__gameboard[7-i][j]] if self.__gameboard[7-i][j]!=None else " "} ",end="")
            print("|")
            print("-"*33)