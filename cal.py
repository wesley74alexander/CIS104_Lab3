validdigs = ['1','2','3','4','5','6','7','8','9','0','.','-']
validops = ['+','-','*','/','^']
validfuncs = ['i','I','c','C','r','R','m','M','s','S','x','X']

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        print("You can't divide by zero!")
def powr(a, b):
    return a ** b
def clr(val):
    return None
def sto(val):
    stored = val
    print("Saved")
    return stored
def recall(stored):
    val = stored
    return val
def memclr(stored):
    stored = None
    print("Memory Cleared")
    return stored
def inv(val):
    val *= -1
    return val

def calculator_basic(num1, num2, op):
    if op == '+':
        return add(num1, num2)
    elif op == '-':
        return sub(num1, num2)
    elif op == '*':
        return mult(num1, num2)
    elif op == '/':
        return div(num1, num2)
    elif op == '^':
        return powr(num1, num2)

def calculator_funcs(num, func):
    if func in 'i,I':
        return inv(num)
    elif func in 'c,C':
        return clr(num)
    elif func in 's,S':
        return sto(num)
    elif func in 'm,M':
        return memclr(num)
    elif func in 'r,R':
        return recall(num)
