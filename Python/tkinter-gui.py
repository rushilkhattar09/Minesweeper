from Tkinter import *
from random import randint
from time import time, sleep
from PIL import ImageTk

flag = u"\u26F3"

grid_size = map(int, raw_input("Grid dimensions (h w) : ").split())
mine_count = int(raw_input("Number of traps : "))
shades = ['#322', '#422', '#522', '#622', '#722', '#822', '#922', '#a22', '#b22']


# image = Image.open("cartoon_sea_mine.png")

root = Tk()

class tile:
    def __init__(self, a, b):
        self.widget = Button(root, text = ' ', command = self.onclick)
        self.widget.config(font = 'Georgia 12', width = 2, height = 2)
        self.widget.config(bg = shades[0])
        self.coords = [a, b]
        self.widget.bind('<3>', self.rightclicked)
    def onclick(self):
        self.widget.config(relief = SUNKEN)
        if self.coords in grid:
            # photo = ImageTk.PhotoImage("cartoon_sea_mine.gif")
            self.widget.config(text = 'X', fg = 'red')
            # self.widget.image = photo
            endgame()
            return
        count = 0
        adj = list()
        for a in range(self.coords[0]-1, self.coords[0]+2):
            for b in range(self.coords[1]-1, self.coords[1]+2):
                if not isNotValid([a,b]) and [a,b] != self.coords:
                    adj.append([a,b])
        print adj
        count = sum([a in grid for a in adj])
        """
        Equivalent Code
        for a in adj:
            if a in grid:
                count += 1
        """
        self.widget.config(text = str(count))
        if not count:
            root.update()
            sleep(0.1)
            for a in adj:
                display[a[0]][a[1]].onclick()
        return None
    def rightclicked(self, event):
        self.widget.config(text = flag, fg = 'red')

def endgame():
    for a in range(grid_size[0]):
        for b in range(grid_size[1]):
            display[a][b].widget.config(state = DISABLED)
            if (display[a][b].widget.cget('text') == flag):
                if [a,b] in grid:
                    display[a][b].widget.config(fg = 'green')

grid = []
display = [[tile(b,a) for a in range(grid_size[1])] for b in range(grid_size[0])]

def isNotValid(points):
    if points[0] in range(0, grid_size[0]):
        if points[1] in range(0, grid_size[1]):
            if display[points[0]][points[1]].widget.cget('relief') != SUNKEN:
                return 0
            else:
                return 2
    return 1

def mine(a, b):
    display[a][b].config(text = '*', foreground = 'red')


def board():
    for a in range(grid_size[0]):
        for b in range(grid_size[1]):
            display[a][b].widget.grid(row = a, column = b)
            # sleep(0.1)
            # root.update()
    s0, s1 = grid_size
    while (display[-1][-1].widget.cget('bg') != '#b22'):
        for a in range(s0):
            l = [[b,a-b] for b in range(a+1)]
            for i in l:
                n = shades.index(display[i[0]][i[1]].widget.cget('bg'))
                if n < 8:
                    n+=1
                display[i[0]][i[1]].widget.config(bg = shades[n])
            sleep(0.2)
            root.update()

while (len(grid) != mine_count):
    h = randint(0, grid_size[0]-1)
    w = randint(0, grid_size[1]-1)
    if [h,w] not in grid:
        grid.append([h,w])

grid.sort()
print grid

board()

root.mainloop()
