digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
operations = ('+', '-', '*', '/', '^')

def isNumber(unit):
    return all(char in digits for char in unit)

def getOper(operation):
    if operation in ('+', '-'):
        return 0
    elif operation in ('*', '/'):
        return 1
    elif operation == '^':
        return 2

def getRpn(input):
    stack = []
    output = []

    for token in input.split(' '):

        if isNumber(token):
            output.append(token)
            continue

        if token == '(':
            stack.append(token)
            continue

        if token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            continue

        if token in operations:
            opPriority = getOper(token)
            while stack and stack[-1] in operations and getOper(stack[-1]) >= opPriority:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def calcRpn(rpn):
    stack = []

    for token in rpn:
        if isNumber(token):
            stack.append(token)
        else:
            num2 = float(stack.pop())
            num1 = float(stack.pop())
            result = 0

            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = num1 / num2
            elif token == '^':
                result = num1 ** num2

            stack.append(result)

    return stack

if __name__ == '__main__':
    input = '68 / 2 + 124 * 44 * ( 42 / 6 ) ^ 2'
    rpn = getRpn(input)
    
    print("Reverse Polish Notation (RPN):", rpn)
    print("Result:", calcRpn(rpn))