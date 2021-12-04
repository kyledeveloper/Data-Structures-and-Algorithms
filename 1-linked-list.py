import random

class Linkedlist():  
    def __init__(self):
        self.head = None
        self.temphead
        self.temptail

    def settemphead(self):
        self.temhead = self.head
        return self.temhead

    def nodecount(self):
        counter = 1
        temp = self.settemphead()
        while self.head.next!= None:
            counter += 1
            self.head = self.head.next
        self.head = temp
        return counter

    def addNodeInEnd(self):
        randomnum = random.randint(1,101)
        addNode = Node(randomnum)
        while self.head.next!=None:
            self.head = self.head.next
        self.head.next = addNode

    def addNode
        
    def printallNode(self):
        temp = self.settemphead()
        while self.head !=None:
            print(self.head.data)
            self.head = self.head.next
        self.head = temp


class Node():
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None


if __name__ == '__main__':
    # grobal 
    mylistlist1 = Linkedlist()
    mylistlist1.head = Node("Elaine")
    mylistlist1.head.next = Node("Kyle")


    mylistlist1.addNodeInEnd()
    mylistlist1.addNodeInEnd()
    mylistlist1.addNodeInEnd()
    mylistlist1.addNodeInEnd()
    mylistlist1.addNodeInEnd()
    mylistlist1.addNodeInEnd()
    mylistlist1.addNodeInEnd()
    mylistlist1.addNodeInEnd()
    mylistlist1.printallNode()
    
    print(f'total elements in linked list are {mylistlist1.nodecount()}')
    