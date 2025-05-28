from tkinter import *
from PIL import ImageTk, Image
import os

PIECES_IMG = {}
assets_dir = os.path.join(os.path.dirname(__file__), "assets")
for filename in os.listdir(assets_dir):
    if filename.lower().endswith((".png")):
        piece_name = os.path.splitext(filename)[0]
        PIECES_IMG[piece_name] = "./assets/"+filename


class Chess:
    
    def __init__(self):
        self.__gameboard = {}
        self.__images = [] 

    def initializeGame(self):
        for i in range(0,8):
            self.__gameboard[(i,1)] = "WP"
            self.__gameboard[(i,6)] = "BP"
        order = "RNBQKBNR"
        for i in range(0,8):
            self.__gameboard[(i,0)] = "W"+order[i]
            self.__gameboard[(i,7)] = "B"+order[i]
        
        self.__gameboard[(4,1)]=None
        self.__gameboard[(4,3)]="WP"

        self.__gameboard[(4,6)]=None
        self.__gameboard[(4,4)]="BP"

        self.__gameboard[(6,0)]=None
        self.__gameboard[(5,2)]="WN"
    
    def draw(self,root):
        canvas = Canvas(root, width=400, height=400, bg='#dddddd')
        for i in range(8):
            for j in range(4):
                canvas.create_rectangle(50*((i+1)%2)+100*j,50*i,50+50*((i+1)%2)+100*j,50+50*i, fill="#aaaaaa",width=0)
        for x,y in self.__gameboard:
            if self.__gameboard[(x,y)]!=None:
                img = PhotoImage(file=PIECES_IMG[self.__gameboard[(x,y)]])
                self.__images.append(img)
                canvas.create_image(50*x,350-50*y,image=img,anchor=NW)
        canvas.pack()
