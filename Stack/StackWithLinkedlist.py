import Linkelist

class Stack:
    def __init__(self) -> None:
        self.data = Linkelist.Linkedlist()
    
    def push(self,data):
        newNode = Linkelist.Node(data)
        self.data.insert(newNode)
    
    def pop(self):
        self.data.delete()
    
    def printStack(self):
        self.data.printNodeinList()
        print("---------")

    def getpeek(self):
        return self.data.head.getdata    
    

if __name__=='__main__':
    mystack = Stack()
    mystack.push("elaine")
    mystack.push("kyle")
    mystack.pop()
    mystack.printStack()

