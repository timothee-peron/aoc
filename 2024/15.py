import utils
import re

utils.DEBUG = False
utils.printInfo()

def extractData(d):
    return d

data = utils.fileToLString(utils.inputFilePath()).strip().split('\n\n')

initialMap, moves = data
moves = "".join(moves.split("\n"))
initialMap = [list(line) for line in initialMap.split('\n')]
H, W = len(initialMap), len(initialMap[0])

printEnabled = True
def printMap(walls, boxes, robot, move = None, part=1):
    if not utils.DEBUG or not printEnabled:
        return
    print("")
    if move is not None:
        print(f"Move {move}:")
    else:
        print("Initial state:")
    for y in range(H):
        for x in range(W * part):
            pos = (x,y)
            if part == 1:
                print("@" if pos == robot else "#" if pos in walls else "O" if pos in boxes else ".", end="")
            else:
                print("@" if pos == robot else "#" if pos in walls else "[" if pos in boxes else "]" if (x-1,y) in boxes else ".", end="")
        print("")
    print("")

def initData(part = 1):
    _walls = set()
    _boxes = set()
    _robot = None
    for y, line in enumerate(initialMap):
        for x, c in enumerate(line):
            x *= part
            if c == "#":
                _walls.add((x,y))
            elif c == "O":
                _boxes.add((x,y))
            elif c == "@":
                _robot = (x,y)
            
            if part == 1:
                continue
            
            x += 1
            if c == "#":
                _walls.add((x,y))

    assert _robot is not None
    return (_walls, _boxes, _robot)


def applyMove(c, walls, boxes, robot):
    u,v = 0,0
    if c == "^":
        v = -1
    elif c == "v":
        v = +1
    elif c == ">":
        u = +1
    elif c == "<":
        u = -1
    else:
        raise Exception("bad move")
    assert u != 0 or v != 0

    movingBoxes = []
    x, y = robot
    while 0 <= x < W and 0 <= y < H:
        x += u
        y += v
        if (x,y) in walls:
            return walls, boxes, robot
        
        if (x,y) not in boxes:
            # empty space
            break

        movingBoxes.append((x,y))
    
    x, y = robot
    robot = (x+u, y+v)
    if len(movingBoxes) > 0:
        boxes.remove(movingBoxes[0])
        boxes.add((movingBoxes[-1][0]+u, movingBoxes[-1][1]+v))

    return walls, boxes, robot

walls, boxes, robot = initData(1)
printMap(walls, boxes, robot, None)
for move in moves:
    walls, boxes, robot = applyMove(move, walls, boxes, robot)
    printMap(walls, boxes, robot, move)

s = 0
for box in boxes:
    x,y = box
    s += 100*y + x
print(s)


def applyMove2(c, walls, boxes, robot):
    u,v = 0,0
    if c == "^":
        v = -1
    elif c == "v":
        v = +1
    elif c == ">":
        u = +1
    elif c == "<":
        u = -1
    else:
        raise Exception("bad move")
    assert u != 0 or v != 0

    if v != 0:
        return vertivalMove2(c, walls, boxes, robot)
    if v == 0:
        return horizontalMove2(c, walls, boxes, robot)

def horizontalMove2(c, walls, boxes, robot):
    u= 0
    if c == ">":
        u = +1
    elif c == "<":
        u = -1
    else:
        raise Exception("bad move")

    movingBoxes = set()
    x, y = robot
    while 0 <= x < 2*W and 0 <= y < H:
        x += u
        if (x,y) in walls:
            return walls, boxes, robot

        if u == 1:
            if (x,y) in boxes:
                movingBoxes.add((x,y))
                x += u
                continue
            else:
                break
        if u == -1:
            if (x,y) in boxes or (x + u,y) in boxes:
                movingBoxes.add((x,y) if (x,y) in boxes else (x + u,y))
                continue
            else:
                break
    
    x, y = robot
    robot = (x+u, y)
    toAddBoxes = set()
    for box in movingBoxes:
        x,y = box
        toAddBoxes.add((x+u,y))
        boxes.remove(box)
    for box in toAddBoxes:
        boxes.add(box)

    return walls, boxes, robot


def vertivalMove2(c, walls, boxes, robot):
    v = 0
    if c == "^":
        v = -1
    elif c == "v":
        v = +1
    else:
        raise Exception("bad move")

    movingBoxes = set()
    x, y = robot
    checks = set([(x,y)])
    while 0 <= x < 2*W and 0 <= y < H:
        checks = set((x, y +v) for (x,y) in checks)

        for (x,y) in checks:
            if (x,y) in walls:
                return walls, boxes, robot
        
        allEmpty = True
        newChecks = set()
        for (x,y) in checks:
            if (x,y) in boxes:
                newChecks.add((x,y))
                newChecks.add((x+1,y))
                movingBoxes.add((x,y))
                allEmpty = False
            elif (x-1,y) in boxes:
                newChecks.add((x-1,y))
                newChecks.add((x,y))
                movingBoxes.add((x-1,y))
                allEmpty = False

        checks = set()
        for c in newChecks:
            checks.add(c)
        
        if allEmpty:
            break

    
    x, y = robot
    robot = (x, y+v)
    for box in movingBoxes:
        boxes.remove(box)
    for box in movingBoxes:
        boxes.add((box[0], box[1]+v))

    return walls, boxes, robot

playEnabled = False

import getch as gh
from time import sleep

walls, boxes, robot = initData(2)
printMap(walls, boxes, robot, None, 2)
for move in moves:
    walls, boxes, robot = applyMove2(move, walls, boxes, robot)
    if playEnabled:
        print("\033c")
    printMap(walls, boxes, robot, move, 2)
    if playEnabled:
        sleep(0.1)


s = 0
for box in boxes:
    x,y = box
    s += 100*y + x
print(s)

playEnabled = False

if not playEnabled:
    exit(0)

walls, boxes, robot = initData(2)
while True:
    print("\033c")
    printMap(walls, boxes, robot, None, 2)
    ch = gh.getch()
    if ch == 'q':
        break
    if ch == 'r':
        walls, boxes, robot = initData(2)
        continue
    
    if ord(ch) == 65:
        ch = "^"
    elif ord(ch) == 66:
        ch = "v"
    elif ord(ch) == 67:
        ch = ">"
    elif ord(ch) == 68:
        ch = "<"
    else:
        continue
        # raise Exception(f"unexpected char {ord(ch)}")
    walls, boxes, robot = applyMove2(ch, walls, boxes, robot)
