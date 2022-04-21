def isint(test):
    if type(test) == int:
        return True
    else:
        return False

def isNode(test):
    if type(test) == Node:
        return True
    else:
        return False

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    def setNext(self,newNode):
        self.next = newNode
    
    def getNext(self):
        return self.next

    def getdata(self):
        return self.data
    

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def insert(self,data, index = 0):
        newNode = Node(data)
        self.count +=1
        if self.count == 0:
            self.head = newNode
            return
        if index == 0 :
            temp = self.head
            self.head = newNode
            self.head.setNext(temp)
            return
        if index == -1:
            currentNode = self.head
            while currentNode.getNext() != None:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)
            return
        if isint(index):
            counter = 0
            currentNode = self.head
            while counter != index-1:
                currentNode = currentNode.next
                counter += 1
            temp = currentNode.next
            currentNode.setNext(newNode)
            currentNode.getNext().setNext(temp)
            return 


    def pop(self, index = 0):
        if self.count == 0:
            print("Emtpy, Nothing to delete")
            return 
        self.count -=1
        if index == 0:
            temp = self.head
            self.head = self.head.next
            return temp
        elif index == -1:
            currentNode = self.head
            previousNode = None
            while currentNode.getNext() != None:
                previousNode = currentNode
                currentNode = currentNode.getNext()
            previousNode.setNext(None)
            return currentNode
        else:
            currentNode = self.head
            counter = 0
            previousNode = None
            while counter != index:
                counter +=1
                previousNode = currentNode
                currentNode = currentNode.getNext()
            previousNode.setNext(currentNode.getNext())
            return currentNode
                
    
    def printNodeinList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.getdata())
            currentNode = currentNode.next
            

if __name__ == '__main__':
    mylist = Linkedlist()
    mylist.insert("kyle")
    mylist.insert("elaine")
    mylist.insert("kk", 1)
    mylist.insert("ee", 3)
    mylist.insert("hugo",-1)
    mylist.printNodeinList()
    mylist.pop(1)
    mylist.printNodeinList()