"""
Minesweeper written in python 2.7 with Tkinter for UI
"""

# The included modules and their functions
from Tkinter import *
from random import randint
from time import time, sleep

# Constants
flag = u"\u26F3"
mine = 'X'
shades = ['#322', '#422', '#522', '#622', '#722', '#822', '#922', '#a22', '#b22']
size = 10, 10
H, W = 500, 500
S = 40

root = Tk()
root.title(string = 'Minesweeper')
root.config(bg = '#122')
# Graph = Frame(root, height = 180, width = 500)
# Graph.grid(row = 4, column = 0, columnspan = 6)
#
# m,h,w = 10,180, 400
#
# alpha = [chr(b) for b in range(65, 91)]+[chr(b) for b in range(48,58)]
#
# canvas = Canvas(root, height = h, width = w, bg = "#000")
#
# for a,b in enumerate(alpha):
#     canvas.create_text((a+2.25)*m, h-10, text = b, fill = "#fa5", font = "Helvetica 8")
#
# canvas.pack()
# freq = {'0':0.1, '1':0.2, '2':0.3, '3':0.4, '4':0.5, '5':0.6, '6':0.7, '7':0.8, '8':0.9}
# for (b,c) in freq.items():
#     if ord(b)>64:
#         a = ord(b)-65
#     else:
#         a = ord(b)-22
#     # Replacing old bars with new data bars
#     canvas.delete(b)
#     canvas.create_rectangle((a+2)*m, h-20, (a+2.5)*m, h-20-(c*150), fill = shades[int(b)], tag = b)
#     canvas.update()
#     sleep(1)

class tile:
    def __init__(self, coords):
        self.xy = coords
        self.widget = Button(root, text = ' ', command = self.clicked)
        self.widget.config(font = 'Georgia 12', width = 2, height = 2)
    def clicked(self):
        pass

title = Label(root, text = "Minesweeper",
            font = 'Arial 15', height = 3,
            fg = 'Azure', bg = '#122')
title.grid(row = 0, column = 0)
div = Frame(root, height = H, width = W)
div.grid(row = 1, column = 0)
view = Canvas(div, height = H, width = W, bg = '#122')
view.pack()

grid = list()
for a in range(size[0]):
    grid.append(list())
    for b in range(size[1]):
        grid[a].append(' ')

for a in range(size[0]):
    for b in range(size[1]):
        x1, y1 = 50 + (b*S), 50 + (a*S)
        view.create_rectangle(x1, y1, x1+S, y1+S, fill = shades[8])
        view.update()
        sleep(0.2)

root.mainloop()
