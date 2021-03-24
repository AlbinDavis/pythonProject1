class Employee:
    def __init__(self,name,empid):
        self.name=name
        self.id=empid
    def calc(self):
        if self.id<0:
            print("invalid")
        else:
            print("true")

emp1=Employee("alen",-123)
emp1.calc()
emp2=Employee("albin",123)
emp2.calc()

