import utils

utils.DEBUG = False
utils.printInfo()

reg, instr = utils.fileToLString(utils.inputFilePath()).strip().split('\n\n')

assert(utils.numberInString("dsfisf-45odsufh") == -45)
assert(utils.digitsInString("AAA: 1,2,3,4") == (1,2,3,4))

reg = list(map(utils.numberInString, reg.split('\n')))

instr = utils.digitsInString(instr)

# print(rega, regb,regc, instr)



def getOperand(x, regs):
    rega, regb, regc = regs
    if x <= 3:
        return x
    if x == 4:
        return rega
    if x == 5:
        return regb
    if x == 6:
        return regc
    if x == 7:
        raise Exception("oops")
    
    raise Exception("Integer overflow")

def adv(a, regs):
    rega, regb, regc = regs
    regs[0] = rega // (1<<a)

def bxl(a,regs):
    rega, regb, regc = regs
    b = regb
    regs[1] = a ^ b

def bst(a, regs):
    regs[1] = a % 8

def jnz(a, regs):
    rega, regb, regc = regs
    return a if rega != 0 else None

def bxc(a, regs):
    rega, regb, regc = regs
    regs[1] = regb ^ regc

def out(a, regs):
    return a%8

def bdv(a, regs):
    rega, regb, regc = regs
    regs[1] = rega // (1<<a)

def cdv(a, regs):
    rega, regb, regc = regs
    regs[2] = rega // (1<<a)


def execute(initReg, instructions):
    regs = list(initReg)
    output = []

    i = 0
    while 0 <= i and i < len(instructions):
        operation = instructions[i]
        literal = instructions[i+1]

        if operation == 3:
            p = jnz(literal, regs)
            if p != None:
                i = p
                continue
        elif operation == 1:
            bxl(literal, regs)
            i += 2
            continue

        operand = getOperand(instructions[i+1], regs)
        if operation == 0:
            adv(operand, regs)
        if operation == 2:
            bst(operand, regs)
        if operation == 4:
            bxc(operand, regs)
        if operation == 5:
            output.append(out(operand, regs))
        if operation == 6:
            bdv(operand, regs)
        if operation == 7:
            cdv(operand, regs)

        i += 2
    return (tuple(output), tuple(regs))

assert(execute((0,0,9), (2,6)) == (tuple(), (0,1,9)))
assert(execute((10,0,0), (5,0,5,1,5,4)) == ((0,1,2), (10,0,0)))
assert(execute((2024,0,0), (0,1,5,4,3,0))[0] == (4,2,5,6,7,7,7,7,3,1,0))
assert(execute((2024,0,0), (0,1,5,4,3,0))[1][0] == 0)
assert(execute((0,29,0), (1,7))[1][1] == 26)
assert(execute((0,2024,43690), (4,0))[1][1] == 44354)

print(",".join(map(str,execute(reg, instr)[0])))