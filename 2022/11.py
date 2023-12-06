import utils
from collections import defaultdict

# from sortedcontainers import *

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
wholeFile = utils.fileToLString(utils.inputFilePath())

_monkeys = wholeFile.split("\n\n")


def generateInitialStates():
    monkeys = []
    for monkey in _monkeys:
        lines = monkey.split("\n")

        items = lines[1].split(": ")[1]
        items = items.split(", ")
        items = list(map(lambda x: int(x), items))

        op = lines[2].split(": ")[1].split(" ")

        test = lines[3].split(": ")[1].split(" ")[2]
        throwTrue = lines[4].split(": ")[1].split(" ")
        throwFalse = lines[5].split(": ")[1].split(" ")

        _m = {
            "items": items,
            "operationOperator": op[3],  # + or *
            "operationValue": op[4],  # "old" or int
            "testDivisible": int(test),
            "throwTrue": int(throwTrue[3]),
            "throwFalse": int(throwFalse[3]),
        }

        monkeys.append(_m)
    return monkeys;


monkeys = generateInitialStates()

# part 1

activity = [0] * len(monkeys)

for step in range(20):
    # print(f"round {step}")
    # monkeyNum > items
    throwing = defaultdict(list)
    for i in range(len(monkeys)):
        _m = monkeys[i]
        for item in _m["items"]:
            worry = item
            opRight = item if _m["operationValue"] == "old" else int(_m["operationValue"])
            op = _m["operationOperator"]
            if op == "*":
                worry *= opRight
            elif op == "+":
                worry += opRight
            else:
                raise "unsupported"
            worry //= 3
            condition = True if worry % _m["testDivisible"] == 0 else False
            sendTo = _m["throwTrue"] if condition else _m["throwFalse"]
            throwing[sendTo].append(worry)
            activity[i] += 1

        _m["items"] = []
        for throwingTo, items in throwing.items():
            for item in items:
                monkeys[throwingTo]["items"].append(item)
        throwing.clear()

    # for i in range(len(monkeys)):
    #     print(f"\t monkey {i}: " + str(monkeys[i]["items"]))

print("PART 1")
# print(activity)
activity.sort()
print(activity[-1] * activity[-2])

# part 2!!

monkeys = generateInitialStates()
activity = [0] * len(monkeys)
modulo = 1
for _m in monkeys:
    modulo *= _m["testDivisible"]

for step in range(10000):
    # print(f"round {step}")
    # monkeyNum > items
    throwing = defaultdict(list)
    for i in range(len(monkeys)):
        _m = monkeys[i]
        for item in _m["items"]:
            worry = item
            opRight = item if _m["operationValue"] == "old" else int(_m["operationValue"])
            op = _m["operationOperator"]
            if op == "*":
                worry *= opRight
            elif op == "+":
                worry += opRight
            else:
                raise "unsupported"
            worry %= modulo
            condition = True if worry % _m["testDivisible"] == 0 else False
            sendTo = _m["throwTrue"] if condition else _m["throwFalse"]
            throwing[sendTo].append(worry)
            activity[i] += 1

        _m["items"] = []
        for throwingTo, items in throwing.items():
            for item in items:
                monkeys[throwingTo]["items"].append(item)
        throwing.clear()

print("PART 2")
# print(activity)
activity.sort()
print(activity[-1] * activity[-2])
