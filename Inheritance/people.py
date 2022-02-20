class people:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(f"Your name is {self.fname} {self.lname}")

class student(people):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname, lname)
        self.id = None


newstudent = student("Kyle","liang")
newstudent.printName()