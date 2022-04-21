class linkedList():
    def __init__(self,val = 0, next = None) -> None:
        self.val = val
        self.next = next
    def __str__(self):
        return f'{self.val}'
    

head = linkedList(1)
head.next = linkedList(2)
head.next.next = linkedList(3)

def reverse(head):
    if head.next == None or head == None:
        return head
    last = reverse(head.next)
    head.next.next = head
    head.next = None
    print(last)
    return last

reverse(head)