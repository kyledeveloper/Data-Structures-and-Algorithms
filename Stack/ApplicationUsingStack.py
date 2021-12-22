import StackWithLinkedlist

def ismatch(stack,symbols):
    peeksymbols = stack.getpeek()
    if peeksymbols == '{':
        if symbols == '}':
            return True
    if peeksymbols == '(':
        if symbols == ')':
            return True
    if peeksymbols == '[':
        if symbols == ']':
            return True
    else:
        return False
    
def getUserinput():
    return input('Enter something:\n')

def checkbalance():
    balance = False
    userinput = getUserinput()
    if '{' or '[' or '(' in userinput:
        myStack = StackWithLinkedlist.Stack()
        for symbols in userinput:
            if symbols in ['{','[','(']:
                myStack.push(symbols)
                continue
            if symbols in ['}',']',')']:
                if ismatch(myStack,symbols):
                    myStack.pop()
                    continue
                else:
                    return balance
        balance = True
        return balance

    else:
        print("Invaild input")
        return balance

    
print(checkbalance())