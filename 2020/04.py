import utils
import re

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLString(utils.inputFilePath())
passorts = inputLines.split('\n\n')
passorts = [p.replace('\n', ' ') for p in passorts]
passorts = [p.split(' ') for p in passorts]
passorts = [dict([kv.split(':') for kv in p]) for p in passorts]

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
mandFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

valids = 0
for p in passorts:
    k = set(p.keys())
    for f in mandFields:
        if not f in k:
            break
    else:
        valids +=1
print(valids)

eyeColors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
hclRe = re.compile('^#[0-9a-f]{6}$')
pidRe = re.compile('^[0-9]{9}$')

rules = {
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    "byr": lambda v: 1920 <= int(v) <= 2002,
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    "hgt": lambda v: (v.endswith('cm') and 150 <= int(v[0: len(v) - 2]) <= 193) or (v.endswith('in') and 59 <= int(v[0: len(v) - 2]) <= 76),
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "hcl": lambda v: hclRe.match(v) is not None,
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "ecl": lambda v: v in eyeColors,
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    "pid": lambda v: pidRe.match(v) is not None,
}

valids = 0
for p in passorts:
    k = set(p.keys())
    for f in mandFields:
        if not f in k:
            break
        if not rules[f](p[f]):
            break
    else:
        valids +=1
print(valids)
