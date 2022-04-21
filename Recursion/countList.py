class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None

    def getNext(self):
        return self.next
    
    def setNext(self,node):
        self.next = node
    
    def setData(self,data):
        self.data = data
    
    def getData(self):
        return self.data

class Simplelinklist:
    def __init__(self,node) -> None:
        self.head = node

n1 = Node(5)
n2 = Node(9)
n3 = Node(2)
n1.setNext(n2)
n2.setNext(n3)

def countllist(list):
    if list == None:
        return 0    
    else:
        return (1 + countllist(list.getNext()))

print(countllist(n1))

def searchElement(list, target):
    if list == None:
        return False
    elif list == target:
        return  True
    else :
        searchElement(list.getNext(),target)