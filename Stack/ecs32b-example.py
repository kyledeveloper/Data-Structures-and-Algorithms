class Stack2:
    def __init__(self, size):
        self.items = [0 for i in range(size)]
        self.sp = -1
    def isEmpty(self):
        return self.sp == -1
    def push(self, item):
        self.sp = self.sp + 1
        self.items[self.sp] = item
    def pop(self):
        answer = self.items[self.sp]
        self.sp = self.sp - 1
        return answer
    def peek(self):
        return self.items[self.sp]
    def size(self):
        return self.sp + 1

newstack = Stack2(10)
print(newstack.isEmpty())
