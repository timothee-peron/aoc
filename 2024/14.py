import utils
import re

#utils.DEBUG = True
utils.printInfo()

W = 11 if utils.DEBUG else 101
H = 7 if utils.DEBUG else 103

reCompiled = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
def extractData(robot):
    return [int(i) for i in reCompiled.match(robot).groups()]


data = [extractData(robot.strip()) for robot in utils.fileToLString(utils.inputFilePath()).strip().split('\n')]

STEPS = 100
robots = []
for x,y,u,v in data:
    robots.append(((x + 100*u) % W, (y + 100*v) % H))

counts = [0,0,0,0]
W2 = W//2
H2 = H//2
for x, y in robots:
    if y < H2:
        if x < W2:
            counts[0] += 1
        elif x > W2:
            counts[1] += 1
    elif y > H //2:
        if x < W2:
            counts[2] += 1
        elif x > W2:
            counts[3] += 1
print(counts[0] * counts[1] * counts[2] * counts[3])

print("\n\n")

for i in range(10000):
    robots = []
    for x,y,u,v in data:
        robots.append(((x + i*u) % W, (y + i*v) % H))
    pos = set()
    for x, y in robots:
        pos.add((x,y))
    
    drawing = ""
    for y in range(H):
        for x in range(W):
            drawing += "#" if (x,y) in pos else " "
        drawing+="\n"
    
    if "##########" in drawing:
            
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print(i)
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print(drawing)
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print(i)
        print("-------------------------------------------------------------------------------------------------------------------------------\n\n")
        break

print("step 1 solution was ")
print(counts[0] * counts[1] * counts[2] * counts[3])