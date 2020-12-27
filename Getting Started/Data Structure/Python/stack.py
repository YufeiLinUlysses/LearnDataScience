class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def test():
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())


def checkParenthesis(symbols: str) -> bool:
    def matches(open, close):
        d = {"(": ")", "[": "]", "{": "}"}
        return d[open] == close
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbols) and balanced:
        c = symbols[i]
        if c in "([{":
            s.push(c)
        else:
            if s.isEmpty():
                return False
            top = s.pop()
            if not matches(top, c):
                balanced = False
        i += 1
    if balanced and s.isEmpty():
        return True
    return False

# Up to base 16


def decimalToBase(num: int, base: int) -> str:
    s = Stack()
    digits = "0123456789ABCDEF"
    while num > 0:
        s.push(num % base)
        num //= base
    result = ""
    while not s.isEmpty():
        result += str(digits[s.pop()])
    return result


def toPostFix(operations: str) -> str:
    # Marks the priority of each operator, with 3 as the highest
    operators = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }
    # Save operators
    s = Stack()
    # Save values
    l = []
    # Separate strings
    allTokens = [c for c in operations]

    for t in allTokens:
        # Acquire all nums or variables
        if t.isalpha() or t in "0123456789":
            l.append(t)
        elif t == "(":
            s.push(t)
        elif t == ")":
            cur = s.pop()
            while cur != "(":
                l.append(cur)
                cur = s.pop()
        else:
            while (not s.isEmpty()) and (operators[s.peek()] >= operators[t]):
                l.append(s.pop())
            s.push(t)
    while not s.isEmpty():
        l.append(s.pop())
    return " ".join(l)


def postFixEval(expr: str) -> float:

    def doMath(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        return op1 - op2

    s = Stack()
    allTokens = expr.split()

    for t in allTokens:
        if t in "0123456789":
            s.push(int(t))
        else:
            op2 = s.pop()
            op1 = s.pop()
            result = doMath(t, op1, op2)
            s.push(result)
    return s.pop()
