class Stack:
    def __init__(self,size = 10) -> None:
        self.size = size
        # using list to store data, but what if use linked list?
        self.data = []

    def printStack(self) -> str:
        # len() return number of element in list, However, list's indexing is begin with 0 and end will number of element-1 

        index = len(self.data)
        while index > 0:
            print(f"   {self.data[index-1]}   ")
            index -= 1 
        print("-------------")
        
    
    def push(self,item):
        if len(self.data)>= self.size:
            print("Stack overflow!")
        else:
            # append item as the last element of the list
            self.data.append(item)
    
    def pop(self):
        # 0 can be change if there are minimum size of the stack
        if len(self.data) == 0: 
            print("Stack underflow!")
        else:
            # pop the last element of the list
            return self.data.pop(-1)

    def getpeek(self):
        if len(self.data) == 0:
            print("No element in this stack")
        else:
            return self.data[-1]

    def getsize(self):
        return len(self.data)
    
    def changesize(self, size):
        self.size = size


myStack = Stack()
myStack.push("elain")
myStack.push("kyle")
myStack.push("ee")
myStack.push("kk")
myStack.printStack()
myStack.pop()
myStack.printStack()

# disadvantage of using lise (array) to store data.
# first of all, size of array normally can no be change, and if we want to increase the size, it's costly with O(n^2)
