from random import randint
from time import time

grid_size = map(int, raw_input("Grid dimensions (h w) : ").split())
mine_count = int(raw_input("Number of traps : "))

grid = list()
isAlive = True
mineFound = 0
disp_count = 0
display = [[' ' for a in range(grid_size[1])] for b in range(grid_size[0])]
error = {1 : "Remember to click inside the grid!!!", 2 : "You clicked there already!"}


def isNotValid(points):
    if points[0] in range(0, grid_size[0]):
        if points[1] in range(0, grid_size[1]):
            if display[points[0]][points[1]] == ' ':
                return 0
            else:
                return 2
    return 1

def view():
    global disp_count
    disp_count = 0
    print '+ ' + '- + '*grid_size[1]
    for a in range(grid_size[0]):
        print '|',
        for b in range(grid_size[1]):
            disp_count += display[a][b].isdigit()
            print display[a][b],'|',
        # print '|'
        print
        print '+ ' + '- + '*grid_size[1]
    # print '+ ' + '- '*grid_size[1] + '+'

def analyse(point):
    count = 0
    adj = list()
    for a in range(point[0]-1, point[0]+2):
        for b in range(point[1]-1, point[1]+2):
            if not isNotValid([a,b]) and [a,b] != point:
                adj.append([a,b])
    count = sum([a in grid for a in adj])
    print adj, count
    display[point[0]][point[1]] = str(count)
    if not count:
        for a in adj:
            analyse(a)
    return None

while (len(grid) != mine_count):
    h = randint(0, grid_size[0]-1)
    w = randint(0, grid_size[1]-1)
    if [h,w] not in grid:
        grid.append([h,w])

grid.sort()
print grid

view()
print "Begin clicking, so to speak..."
t = time()
while (isAlive):
    click = map(int, raw_input().split())
    if len(click) == 1:
        continue
    click = [click[0]-1, click[1]-1]
    # print click
    if isNotValid(click):
        print error[isNotValid(click)]
        continue
    if click in grid:
        isAlive = False
        break
    analyse(click)
    view()
    print "Opened = %d" % (disp_count)
    if (mine_count == mineFound):
        break
    if (disp_count + mine_count == grid_size[0]*grid_size[1]):
        break
if (isAlive):
    print "Congrats, you survived!"
    print "Your score is %d" % (round(10000/(time()-t), 0))

else:
    print "BOOM"
