import utils

utils.DEBUG = True
utils.printInfo()

fp = utils.inputFilePath()
data = list(map(lambda l: l.split('\n'), utils.fileToLString(fp).strip().split('\n\n')))

workflows = {}
for wf in data[0]:
    name = wf[0: wf.find('{')]
    instr = wf[wf.find('{') + 1 : - 1].split(',')
    workflows[name] = instr

parts = []
for part in data[1]:
    part = part[1:-1].split(',')
    partData = {}
    for p in part:
        p = p.split('=')
        letter, num = p
        partData[letter] = int(num)
    parts.append(partData)

# return True / False if part accepted / rejected, name of the next workflow otherwise
def nextWorkflow(part, step, workflows):
    for condition in workflows[step]:
        if condition == 'A':
            return True
        if condition == 'R':
            return False
        if condition.find('>') == -1 and condition.find('<') == -1:
            return condition # it's another wf
        char = ''
        if condition.find('<') != -1:
            char = '<'
        if condition.find('>') != -1:
            char = '>'
        
        prop, remain = condition.split(char)
        value, ternary = remain.split(':')
        value = int(value)

        # prop=value:ternary

        propVal = part[prop]

        condition = (char == '<' and propVal < value) or (char == '>' and propVal > value)

        if not condition:
            continue
        
        if ternary == 'A':
            return True
        if ternary == 'R':
            return False
        
        return ternary



accepted = []
for part in parts:
    step = 'in'
    
    while type(step) == str:
        step = nextWorkflow(part, step, workflows)
    
    if step:
        accepted.append(part)

score = 0
for part in accepted:
    score += sum(part.values())

print(score)
