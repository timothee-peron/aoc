import z3
import utils
import re

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

lines = utils.fileToLines(utils.inputFilePath())

s = z3.Solver()
variables = {}
for line in lines:
  regex = r'[a-z]+'
  words = re.findall(regex, line)
  for word in words:
    if word not in variables.keys():
      variables[word] = z3.Int(word)

  for word in words:
    line = line.replace(word, f"variables['{word}']")

  line = line.replace(':', ' ==')

  # print(line)
  s.add(eval(line))

result = s.check()
resultModel = s.model()

print('PART1')
print(resultModel.eval(z3.Int("root")))



s = z3.Solver()
variables = {}
for line in lines:
  if line.startswith("humn:"):
    variables["humn"] = z3.Int("humn")
    continue

  if line.startswith("root:"):
    line = line.split(': ')[1]
    line = line.replace('+', '==')

  regex = r'[a-z]+'
  words = re.findall(regex, line)
  for word in words:
    if word not in variables.keys():
      variables[word] = z3.Int(word)

  for word in words:
    line = line.replace(word, f"variables['{word}']")

  line = line.replace(':', ' ==')

  # print(line)
  s.add(eval(line))

for k, v in variables.items():
  s.add(v > 0)

# because I had 2 solutions?!
s.add(variables['humn'] < 3876907167496)
# s.add(variables['humn'] < 3876907167495)


result = s.check()
resultModel = s.model()

print('PART2')
# print(resultModel)
print(resultModel.eval(z3.Int("humn")))

# for k, v in variables.items():
#   print(k + ": " + str(resultModel.eval(v)))
