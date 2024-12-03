import utils
import re

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath())

pattern = re.compile(r'^(\d+),(\d+)\)')

s = 0
for part in data.split("mul("):
  if match := pattern.search(part):
    s += int(match.group(1)) * int(match.group(2))

print(s)


pattern = re.compile(r'^(\d+),(\d+)\)')

s = 0
i = 0
enabled = True
while i < len(data):
  if data[i: i+4] == "do()":
    i += 4
    enabled = True
    continue

  if data[i: i+7] == "don't()":
    i += 7
    enabled = False
    continue

  if enabled and data[i: i+4] == "mul(":
    i += 4

    section = data[i:]

    if match := pattern.search(section):
      s += int(match.group(1)) * int(match.group(2))

    continue

  i+=1

print(s)
