from tkinter import *
from chess import Chess

root = Tk()
root.title("Chess")
root.geometry("400x400")

game = Chess()
game.initializeGame()

game.draw(root)

root.mainloop()