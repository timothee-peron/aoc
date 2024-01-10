import utils

# utils.DEBUG = True
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
def nextWorkflow(_part, _step, _workflows):
    for condition in _workflows[_step]:
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

        propVal = _part[prop]

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

    while isinstance(step, str):
        step = nextWorkflow(part, step, workflows)

    if step:
        accepted.append(part)

score = 0
for part in accepted:
    score += sum(part.values())

print(score)
if utils.DEBUG:
    assert score == 377025


# part 2
def getAccepted(workflows):
    accepted = []
    queue = {}
    queue['in'] = {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}

    while queue:
        # print(queue)

        # remove R and A from queue
        queue.pop('R', None)
        a = queue.pop('A', None)
        if a is not None:
            accepted.append(a)

        if not queue:
            break

        name, partIntervals = queue.popitem()
        wf = workflows[name]

        for condition in wf:

            if condition == 'A':
                accepted.append(partIntervals)
                continue
            if condition == 'R':
                continue

            if condition.find('>') == -1 and condition.find('<') == -1:
                # it's another wf
                queue[condition] = partIntervals.copy()
                break

            char = ''
            if condition.find('<') != -1:
                char = '<'
            if condition.find('>') != -1:
                char = '>'

            prop, remain = condition.split(char)
            value, ternary = remain.split(':')
            value = int(value)

            # prop char value : ternary
            # s    <    1351  : px

            propInterval = partIntervals[prop]
            propA, propB = propInterval

            if char == '<':
                # split the interval
                queue[ternary] = partIntervals.copy()
                if propA <= value - 1:
                  queue[ternary][prop] = (propA, value - 1)
                if value <= propB:
                  partIntervals[prop] = (value, propB)
            else:
                # split the interval
                queue[ternary] = partIntervals.copy()
                if value + 1 <= propB:
                  queue[ternary][prop] = (value + 1, propB)
                if propA <= value:
                  partIntervals[prop] = (propA, value)

    return accepted

def countAccepted(accepted):
    count = 0
    for a in accepted:
        p = 1
        for x, y in a.values():
            p *= (y-x) + 1
        count += p
    return count

assert getAccepted({'in': ['a<2000:A', 'R']}) == [{'x': (1, 4000), 'm': (1, 4000), 'a': (1, 1999), 's': (1, 4000)}]
assert getAccepted({'in': ['a>2000:A', 'R']}) == [{'x': (1, 4000), 'm': (1, 4000), 'a': (2001, 4000), 's': (1, 4000)}]
assert getAccepted({'in': ['a<2000:R', 'A']}) == [{'x': (1, 4000), 'm': (1, 4000), 'a': (2000, 4000), 's': (1, 4000)}]
assert getAccepted({'in': ['a>2000:R', 'A']}) == [{'x': (1, 4000), 'm': (1, 4000), 'a': (1, 2000), 's': (1, 4000)}]


part2 = countAccepted(getAccepted(workflows))
print(part2)
if utils.DEBUG:
    assert part2 == 167409079868000
else:
    assert part2 == 135506683246673

