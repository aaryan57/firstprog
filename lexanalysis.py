with open("input.txt", "r") as file:
    lines = file.readlines()


keyword=[]
identifier=[]
operator=[]
number=[]
invalid=[]
seperator=[]

def isKeyword(word):
    return word in['int','char','float','break', 'continue', 'string', 'arr']
def isIdentifier(word):
    if not isKeyword(word) and not isNumber(word) and not isOperator(word) and word.isidentifier():
        return True
    return False

def isOperator(word):
    return word in ['=', '+', '<', '>', '-', '*', '/']

def isNumber(word):
    if word.isdigit():
        return True
    elif word.replace('.', '', 1).isdigit():
        return True
    return False

for line in lines:
    t=line.strip()
    print("Code line : ", t)

    if t[-1]==";":
        if t[-1] not in seperator:
            seperator.append(t[-1])

        t=t[:len(t)-1:]

    i=t.split()
    for i in t.split(' '):
        if isKeyword(i):
            if i not in keyword:
                keyword.append(i)

        elif isIdentifier(i):
            if i not in identifier:
                identifier.append(i)

        elif isOperator(i):
            if i not in operator:
                operator.append(i)

        elif isNumber(i):
            if i not in number:
                number.append(i)
        else:
            if i not in invalid and i not in identifier:
                invalid.append(i)
print()
print("keyword : ", keyword)
print("Identifier : ", identifier)
print("Operator : ", operator)
print("Separators : ", seperator)
print("Number Constants", number)
print("Invalid : ", invalid)
