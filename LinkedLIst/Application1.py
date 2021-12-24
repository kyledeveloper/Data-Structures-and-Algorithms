# Find the value of nth node from the end of the Linkedlist

from LinkedList import SimpleLinkedlist

def foundValueofN(linkedlist, n):
    currentNode = linkedlist.head
    lentgh = 0
    while currentNode != None:
        currentNode = currentNode.getNext()
        lentgh += 1
    counter = 0
    currentNode = linkedlist.head
    while counter < lentgh- (n + 1):
        currentNode = currentNode.getNext()
        counter +=1
    return currentNode.getdata()
    # time complicity = O(n)+O(n) = O(n)


if __name__ == '__main__':
    newlist = SimpleLinkedlist()
    # for i in range(1):
    #     randomNum = random.randint(0,101)
    #     newlist.insert(randomNum)
    newlist.insert("ee")
    newlist.insert("kk")
    newlist.insert("mm")
    newlist.insert("hh")
    newlist.printNodeinList()

    print(foundValueofN(newlist, 1))

    # mylist = SimpleLinkedlist()
    # mylist.insert("kyle")
    # mylist.insert("elaine")
    # mylist.insert("mario")
    # mylist.insert("ee", 3)
    # mylist.insert("hugo",-1)
    # mylist.printNodeinList()
    # print(mylist.getlast().getdata())
    # print(mylist.getlast().hasNext())
