WHITE = "W"
BLACK = "B"

PAWN = "P"
BISHOP = "B"
KNIGHT = "N"
ROOK = "R"
QUEEN = "Q"
KING = "K"

PIECES = {
    "BP" : "\u2659",
    "BB" : "\u2657",
    "BR" : "\u2656",
    "BQ" : "\u2655",
    "BK" : "\u2654",
    "BN" : "\u2658",
    "WP" : "\u265f",
    "WN" : "\u265e",
    "WB" : "\u265d",
    "WR" : "\u265c",
    "WQ" : "\u265b",
    "WK" : "\u265a",
    "WN" : "\u265e"
}

def convert(notation):
    if type(notation)==str:
        return (ord(notation[0])-97,8-int(notation[1]))

class Chess:
    def __init__(self):
        self.__gameboard = [[None for i in range(8)] for j in range(8)]
        self.__turn = WHITE

    def initializeGame(self):
        order = "RNBQKBNR"
        for i in range(0,8):
            self.__gameboard[6][i] = "WP"
            self.__gameboard[7][i] = "W"+order[i]
            self.__gameboard[1][i] = "BP"
            self.__gameboard[0][i] = "B"+order[i]

        self.__gameboard[3][3] = "WR"
    
    def draw(self):
        print()
        print("    "+"-"*33)
        for i in range(8):
            print(f"  {8-i} ",end="")
            for j in range(8):
                print(f"| {PIECES[self.__gameboard[i][j]] if self.__gameboard[i][j]!=None else " "} ",end="")
            print("|")
            print("    "+"-"*33)
        print("      A   B   C   D   E   F   G   H  ")
        print()
    
    def isCheckmate(self):
        return False
    
    def move(self,notation):
        try :
            startpos, endpos = notation.split(" ")
            startpos, endpos = convert(startpos), convert(endpos)
            piece = self.__gameboard[startpos[1]][startpos[0]]
        except:
            return False
        if piece==None: return False

        if piece[1]==ROOK:
            if startpos[0] != endpos[0] and startpos[1] != endpos[1]:
                return False

            dx = 0 if startpos[0] == endpos[0] else (1 if endpos[0] > startpos[0] else -1)
            dy = 0 if startpos[1] == endpos[1] else (1 if endpos[1] > startpos[1] else -1)

            x, y = startpos[0] + dx, startpos[1] + dy
            while (x, y) != endpos:
                if self.__gameboard[y][x] is not None:
                    return False
                x += dx
                y += dy

            target = self.__gameboard[endpos[1]][endpos[0]]
            if target is not None and target[0] == piece[0]:
                return False
            self.__gameboard[endpos[1]][endpos[0]] = piece
            self.__gameboard[startpos[1]][startpos[0]] = None

        return True
