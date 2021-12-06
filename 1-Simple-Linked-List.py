import random

class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

def isNode(data):
    if type(data) == Node:
        return True
    else:
        return False
class SimplyLinkedlist():  
    def __init__(self):
        self.head = None
    
        
    def insert(self,num):
        currentNode = self.head
        counter = 1
        while counter != num:
            currentNode = currentNode.next
            counter += 1
        temp = currentNode.next
        randomnum = random.randint(1,101)
        addNode = Node(randomnum)
        currentNode.next = addNode
        currentNode.next.next = temp
        

    def nodecount(self):
        if self.head != None:
            counter = 1
            currentNode = self.head
            while currentNode.next != None:
                counter += 1
                currentNode = currentNode.next
            return counter
        else:
            return 0

    def addNodeAtEnd(self):
        currentNode = self.head
        randomnum = random.randint(1,101)
        addNode = Node(randomnum)
        while currentNode.next!=None:
            currentNode = currentNode.next
        currentNode.next = addNode

    def addNodeAtBegin(self):
        randomnum = random.randint(1,101)
        addNode = Node(randomnum)
        addNode.next = self.head
        self.head = addNode
        
    def printallNode(self):
        currentNode = self.head
        while currentNode !=None:
            print(currentNode.data)
            currentNode = currentNode.next
    
    def delNode(self,num):
        if num == 1:
            self.head = self.head.next
        elif num == -1:
            currentNode = self.head
            previousNode = None
            while currentNode.next != None:
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = None
        else:
            currentNode = self.head
            counter = 1
            previousNode = None
            while counter != num:
                previousNode = currentNode
                currentNode = currentNode.next
                counter +=1
            previousNode.next = currentNode.next

    def cleanup(self):
        while isNode(self.head.next):
            self.delNode(1)
        self.head = None


if __name__ == '__main__':
    mylistlist1 = SimplyLinkedlist()
    mylistlist1.head = Node("Elaine")
    mylistlist1.head.next = Node("Kyle")


    mylistlist1.addNodeAtEnd()
    mylistlist1.addNodeAtEnd()
    mylistlist1.addNodeAtEnd()
    mylistlist1.addNodeAtBegin()
    mylistlist1.addNodeAtBegin()
    mylistlist1.addNodeAtBegin()
    
    mylistlist1.insert(4)
    mylistlist1.delNode(-1)
    mylistlist1.printallNode() 
    print(f'total elements in linked list are {mylistlist1.nodecount()}')
    mylistlist1.cleanup()
    print(mylistlist1.nodecount())

