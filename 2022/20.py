# importing packages
import utils

utils.DEBUG = True
# utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
# wholeFile = utils.fileToLString(utils.inputFilePath())
numbers = [int(x) for x in inputLines]


# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data, pos, next, previous):
        self.data = data
        self.previous = previous
        self.next = next
        self.initialPos = pos

    def __str__(self):
        return f"[ ({self.initialPos}) {self.previous.data} < _{self.data}_ < {self.next.data} ]"


# A Linked List class with a single head node
class RoundLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.initPosDict = {}

    def resetPosDict(self):
        current = self.head
        for i in range(self.count):
            self.initPosDict[i] = current
            current = current.next

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data, self.count, None, None)
        self.initPosDict[self.count] = newNode
        self.count += 1

        if not self.tail:
            # first elem
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.previous = newNode

        newNode.next = self.head
        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.head.previous = self.tail

    # def normalizeNumbers(self):
    #     current = self.head
    #     for _ in range(self.count):
    #         current.data %= self.count - 1
    #         current = current.next

    # print method for the linked list
    def __str__(self):
        current = self.head
        val = ""
        for _ in range(self.count):
            val += " " + str(current.data)
            current = current.next
        return val

    def moveByN(self, pos, n=None):
        if n is None:
            n = self.initPosDict[pos].data

        if n % (self.count - 1) == 0:
            return
        # A (B) C D | E
        # move B after D
        B = self.initPosDict[pos]
        A = B.previous
        C = B.next
        D = B
        for _ in range(n % (self.count - 1)):
            D = D.next
        E = D.next

        # print(f"moving {A.data} ({B.data}) {C.data} {D.data} | {E.data}")

        A.next, C.previous, D.next, E.previous = C, A, B, B
        B.previous, B.next = D, E

        if B == self.head:
            self.head = C

    def at(self, pos):
        current = self.head
        for _ in range(pos % (self.count - 1)):
            current = current.next
        return current


assert (-3 % 7 == 4)

rll = RoundLinkedList()
for n in numbers:
    rll.insert(n)
    # print(f"Adding {n} : {rll}")
# print(rll)

for i, n in enumerate(numbers):
    # print(f"##### {i} ####")
    rll.moveByN(i)
    # print(rll)

print("PART1")
if utils.DEBUG:
    print(rll)

zero = rll.head
while zero.data != 0:
    zero = zero.next

values = []
current = zero
for _ in range(3):
    for _ in range(1000):
        current = current.next
    values.append(current.data)
    # print(current)
print(sum(values))

# PART 2
decription = 811589153

rll = RoundLinkedList()
for n in numbers:
    rll.insert(n * 811589153)

print(rll)
for _ in range(10):
    rll.resetPosDict()
    for i, _ in enumerate(numbers):
        rll.moveByN(i)
    print(rll)
