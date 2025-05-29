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
    else: return notation

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
    
    
    def move(self,notation):
        try :
            startpos, endpos = notation.split(" ")
            startpos, endpos = convert(startpos), convert(endpos)
            piece = self.__gameboard[startpos[1]][startpos[0]]
        except:
            return False
        if piece==None: return False
        if piece[0]!=self.__turn: return False

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
        
        if piece[1]==BISHOP:
            if abs(startpos[0] - endpos[0]) != abs(startpos[1] - endpos[1]):
                return False

            dx = 1 if endpos[0] > startpos[0] else -1
            dy = 1 if endpos[1] > startpos[1] else -1

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
        
        if piece[1]==KNIGHT:
            if (abs(startpos[0] - endpos[0]), abs(startpos[1] - endpos[1])) not in [(1, 2), (2, 1)]:
                return False

            target = self.__gameboard[endpos[1]][endpos[0]]
            if target is not None and target[0] == piece[0]:
                return False
            self.__gameboard[endpos[1]][endpos[0]] = piece
            self.__gameboard[startpos[1]][startpos[0]] = None
        
        if piece[1]==QUEEN:
            dx = endpos[0] - startpos[0]
            dy = endpos[1] - startpos[1]

            if abs(dx) == abs(dy): 
                step_x = 1 if dx > 0 else -1
                step_y = 1 if dy > 0 else -1
                x, y = startpos[0] + step_x, startpos[1] + step_y
                while (x, y) != endpos:
                    if self.__gameboard[y][x] is not None:
                        return False
                    x += step_x
                    y += step_y
            elif dx == 0 or dy == 0:
                step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
                step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
                x, y = startpos[0] + step_x, startpos[1] + step_y
                while (x, y) != endpos:
                    if self.__gameboard[y][x] is not None:
                        return False
                    x += step_x
                    y += step_y
            else:
                return False

            target = self.__gameboard[endpos[1]][endpos[0]]
            if target is not None and target[0] == piece[0]:
                return False
            self.__gameboard[endpos[1]][endpos[0]] = piece
            self.__gameboard[startpos[1]][startpos[0]] = None
        
        if piece[1]==KING:
            if max(abs(startpos[0] - endpos[0]), abs(startpos[1] - endpos[1])) != 1:
                return False

            target = self.__gameboard[endpos[1]][endpos[0]]
            if target is not None and target[0] == piece[0]:
                return False
            self.__gameboard[endpos[1]][endpos[0]] = piece
            self.__gameboard[startpos[1]][startpos[0]] = None
        
        if piece[1]==PAWN:
            direction = -1 if piece[0] == WHITE else 1
            start_row = 6 if piece[0] == WHITE else 1

            dx = endpos[0] - startpos[0]
            dy = endpos[1] - startpos[1]

            target = self.__gameboard[endpos[1]][endpos[0]]

            if dx == 0:
                if dy == direction and target is None:
                    self.__gameboard[endpos[1]][endpos[0]] = piece
                    self.__gameboard[startpos[1]][startpos[0]] = None
                elif dy == 2 * direction and startpos[1] == start_row and \
                     self.__gameboard[startpos[1] + direction][startpos[0]] is None and target is None:
                    self.__gameboard[endpos[1]][endpos[0]] = piece
                    self.__gameboard[startpos[1]][startpos[0]] = None
                else:
                    return False

            elif abs(dx) == 1 and dy == direction and target is not None and target[0] != piece[0]:
                self.__gameboard[endpos[1]][endpos[0]] = piece
                self.__gameboard[startpos[1]][startpos[0]] = None
            else:
                return False

        self.__turn = WHITE if self.__turn == BLACK else BLACK
        return True

    def isCheck(self):
        king_piece = self.__turn + KING
        king_pos = None
        for y in range(8):
            for x in range(8):
                if self.__gameboard[y][x] == king_piece:
                    king_pos = (x, y)
                    break
            if king_pos:
                break
        if not king_pos:
            return False 

        enemy = BLACK if self.__turn == WHITE else WHITE
        for y in range(8):
            for x in range(8):
                piece = self.__gameboard[y][x]
                if piece and piece[0] == enemy:
                    orig = self.__gameboard[king_pos[1]][king_pos[0]]
                    from_piece = self.__gameboard[y][x]
                    self.__gameboard[king_pos[1]][king_pos[0]] = from_piece
                    self.__gameboard[y][x] = None
                    can_attack = False
                    if piece[1] == ROOK:
                        if (x == king_pos[0] or y == king_pos[1]):
                            dx = 0 if x == king_pos[0] else (1 if king_pos[0] > x else -1)
                            dy = 0 if y == king_pos[1] else (1 if king_pos[1] > y else -1)
                            tx, ty = x + dx, y + dy
                            blocked = False
                            while (tx, ty) != king_pos:
                                if self.__gameboard[ty][tx] is not None:
                                    blocked = True
                                    break
                                tx += dx
                                ty += dy
                            if not blocked:
                                can_attack = True
                    elif piece[1] == BISHOP:
                        if abs(x - king_pos[0]) == abs(y - king_pos[1]):
                            dx = 1 if king_pos[0] > x else -1
                            dy = 1 if king_pos[1] > y else -1
                            tx, ty = x + dx, y + dy
                            blocked = False
                            while (tx, ty) != king_pos:
                                if self.__gameboard[ty][tx] is not None:
                                    blocked = True
                                    break
                                tx += dx
                                ty += dy
                            if not blocked:
                                can_attack = True
                    elif piece[1] == QUEEN:
                        dx = king_pos[0] - x
                        dy = king_pos[1] - y
                        if abs(dx) == abs(dy):
                            step_x = 1 if dx > 0 else -1
                            step_y = 1 if dy > 0 else -1
                            tx, ty = x + step_x, y + step_y
                            blocked = False
                            while (tx, ty) != king_pos:
                                if self.__gameboard[ty][tx] is not None:
                                    blocked = True
                                    break
                                tx += step_x
                                ty += step_y
                            if not blocked:
                                can_attack = True
                        elif dx == 0 or dy == 0:
                            step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
                            step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
                            tx, ty = x + step_x, y + step_y
                            blocked = False
                            while (tx, ty) != king_pos:
                                if self.__gameboard[ty][tx] is not None:
                                    blocked = True
                                    break
                                tx += step_x
                                ty += step_y
                            if not blocked:
                                can_attack = True
                    elif piece[1] == KNIGHT:
                        if (abs(x - king_pos[0]), abs(y - king_pos[1])) in [(1, 2), (2, 1)]:
                            can_attack = True
                    elif piece[1] == KING:
                        if max(abs(x - king_pos[0]), abs(y - king_pos[1])) == 1:
                            can_attack = True
                    elif piece[1] == PAWN:
                        direction = 1 if enemy == BLACK else -1
                        if king_pos[1] - y == direction and abs(king_pos[0] - x) == 1:
                            can_attack = True
                    self.__gameboard[y][x] = from_piece
                    self.__gameboard[king_pos[1]][king_pos[0]] = orig
                    if can_attack:
                        return True
        return False