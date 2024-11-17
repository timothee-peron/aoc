import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLString(utils.inputFilePath())

instructions = list(map(int, inputLines.split(',')))

def doProgram(instructions):
    i = 0

    while instructions[i] != 99:
        t = instructions[i]

        if t == 1:
            instructions[instructions[i + 3]] = instructions[instructions[i + 1]] + instructions[instructions[i + 2]]
        elif t == 2:
            instructions[instructions[i + 3]] = instructions[instructions[i + 1]] * instructions[instructions[i + 2]]
        elif t == 99:
            break
        else:
            raise Exception("Invalid code " + str(t))
        i += 4

    return instructions

assert("2,0,0,0,99" == ','.join(map(str, doProgram(list(map(int, "1,0,0,0,99".split(',')))))))
assert("2,3,0,6,99" == ','.join(map(str, doProgram(list(map(int, "2,3,0,3,99".split(',')))))))
assert("2,4,4,5,99,9801" == ','.join(map(str, doProgram(list(map(int, "2,4,4,5,99,0".split(',')))))))
assert("30,1,1,4,2,5,6,0,99" == ','.join(map(str, doProgram(list(map(int, "1,1,1,4,99,5,6,0,99".split(',')))))))

instructions[1] = 12
instructions[2] = 2
print(doProgram(instructions)[0])

goal = 19690720
for i in range(1, 100) :
    for j in range(1, 100) :
        instructions = list(map(int, inputLines.split(',')))
        instructions[1] = i
        instructions[2] = j
        if (goal == doProgram(instructions)[0]):
            print(i*100 + j)
            exit(0)
